import django
import sys

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .modules.edgemanage import edge_query, edge_conf

def index(request):
    return JsonResponse({
        'name': settings.APP_NAME,
        'debug': settings.DEBUG,
        'versions': {
            'django': django.get_version(),
            'python': sys.version
        }
    })


def api_edge_query(request, dnet):
    return JsonResponse(edge_query(dnet), safe=False)


@csrf_exempt
def api_edge_conf(request):
    return JsonResponse(edge_conf(
        request.POST['dnet'],
        request.POST['edge'],
        request.POST['mode'],
        request.POST['comment'],
        request.POST['comment_user']
    ), safe=False)
