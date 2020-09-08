import sys
import django

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

from .modules.edgemanage import edge_query, edge_conf

@api_view(['GET'])
def api_info(request):
    return Response({
        'name': settings.APP_NAME,
        'debug': settings.DEBUG,
        'versions': {
            'django': django.get_version(),
            'python': sys.version
        }
    })


@api_view(['GET'])
def api_edge_query(request):
    try:
        return Response(edge_query(request.GET['dnet']))
    except KeyError as err:
        return Response({"error": str(err)}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST', 'GET'])
def api_edge_conf(request):
    if request.method == 'GET':
        # To display API run page
        return Response({})

    # request.method == 'POST':
    try:
        edge_conf_result = edge_conf(
            request.data['dnet'], request.data['edge'],
            request.data['mode'], request.data['comment'],
            request.data['comment_user'])
        return Response(edge_conf_result, status=status.HTTP_201_CREATED)
    except KeyError as err:
        return Response({"error": str(err)}, status=status.HTTP_404_NOT_FOUND)
    except Exception as err:
        return Response({"error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
