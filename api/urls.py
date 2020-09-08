from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.api_info, name='api_info'),
    path('edge/list', views.api_edge_query, name='api_edge_query'),
    path('edge/config', views.api_edge_conf, name='api_edge_conf'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
