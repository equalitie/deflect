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

        output_data.append((edge_state.mode, edge_state.state,
                            edge_state.health,
                            edge_state.edgename,
                            str(state_time),
                            None if edge_state.comment == "" else edge_state.comment))

    return output_data
