from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edge/query', views.api_edge_query, name='api_edge_query')
]
