import django
import sys

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return JsonResponse({
        'name': settings.APP_NAME,
        'debug': settings.DEBUG,
        'versions': {
            'django': django.get_version(),
            'python': sys.version
        }
    })
