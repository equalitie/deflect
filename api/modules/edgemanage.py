"""
Middleware between API view and EdgemanageAdapter
"""

from django.conf import settings
from edgemanage3.edgemanage.adapter import EdgemanageAdapter
from edgemanage3.edgemanage import EdgeState

import time


def edge_query(dnet=None):
    """
    Perform a `edge_query`
    according to `EDGEMANAGE_CONFIG` and `EDGEMANAGE_DNET`

    - edge_query --dnet mynet --config ../edgemanage_test/edgemanage.yaml -v
    """

    edgemanage_adapter = EdgemanageAdapter(
      settings.EDGEMANAGE_CONFIG, dnet or settings.EDGEMANAGE_DNET)
    output_data = []
    now = time.time()

    for edge in edgemanage_adapter.edge_list:

        edge_state = None

        try:
            edge_state = EdgeState(edge, edgemanage_adapter.get_config("healthdata_store"),
                                   nowrite=True)
        except Exception as e:
            return "failed to load state for edge %s: %s\n" % (edge, str(e))

        if edge_state.state_entry_time:
            state_time = int(now - edge_state.state_entry_time)
        else:
            state_time = -1

        output_data.append({
            'edgename': edge_state.edgename,
            'mode': edge_state.mode,
            'state':  edge_state.state,
            'health': edge_state.health,
            'state_time': state_time,
            'comment': None if edge_state.comment == "" else edge_state.comment
        })

    return output_data


def edge_conf(dnet, edge, mode, comment, comment_user, no_syslog=False):
    """
    Perform a `edge_conf`
    according to `EDGEMANAGE_CONFIG` and `EDGEMANAGE_DNET`

    - edge_conf
        --dnet mynet
        --config edgemanage.yaml
        --mode unavailable
        --comment "out"
        lime20.prod.deflect.ca
    """
    edgemanage_adapter = EdgemanageAdapter(
      settings.EDGEMANAGE_CONFIG, dnet or settings.EDGEMANAGE_DNET)

    # create lock file
    lock, lock_err = edgemanage_adapter.lock_edge_conf()
    if not lock:
        raise Exception(lock_err)

    if edge not in edgemanage_adapter.edge_list:
        raise KeyError("Edge %s is not in the edge list of %s" %
                       (edge, dnet))

    if not edgemanage_adapter.edge_data_exist(edge):
        raise Exception("Edge %s is not initialised yet - not setting "
                        "status" % edge)

    try:
        edge_state = EdgeState(edge,
                               edgemanage_adapter.config["healthdata_store"],
                               nowrite=False)
    except Exception as e:
        raise Exception("failed to load state for edge %s: %s" %
                        (edge, str(e)))

    edge_state.set_mode(mode)

    if comment:
        comment = "[%s] %s" % (comment_user, comment)
        edge_state.set_comment(comment)

        if not no_syslog:
            edgemanage_adapter.log_edge_conf(
                edge, mode, comment
            )

    elif mode == "available":
        edge_state.unset_comment()

    # release lock
    edgemanage_adapter.unlock_edge_conf()
