import django
import sys

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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
def api_edge_query(request, dnet):
    try:
        return Response(edge_query(dnet))
    except KeyError as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST', 'GET'])
def api_edge_conf(request):
    if request.method == 'GET':
        # To display API run page
        return Response({})
    elif request.method == 'POST':
        try:
            edge_conf_result = edge_conf(
                request.data['dnet'], request.data['edge'],
                request.data['mode'], request.data['comment'],
                request.data['comment_user'])
            return Response(edge_conf_result, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

