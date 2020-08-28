# Deflect Core

## Versions

1. Python 3.6.10
2. Django 3.1

## Install

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Init submodule edgemanage
git submodule update --init
cd edgemanage3
python setup.py install
```

## API Implementation Tracker

### GET /api/edgemanage/<str:dnet>

Equivalent to command `edge_query --dnet dnet1`

#### Sample output

```
[
    {
        "edgename": "one22.prod.deflect.ca",
        "mode": "available",
        "state": "out",
        "health": "pass",
        "state_time": -1,
        "comment": null
    }
]
```

### POST /api/edgemanage

#### Param

1. dnet
2. edge: edge hostname
3. mode: available / unavailable
4. comment
5. comment_user

#### Sample output

```
{
    "edge": "lime20.prod.deflect.ca",
    "prev_state": {
        "mode": "available",
        "comment": "[jeremy_pm] hi hi"
    },
    "current_state": {
        "mode": "available",
        "comment": "[jeremy_pm] hi hi"
    }
}
```
