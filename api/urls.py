from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edgemanage/<str:dnet>', views.api_edge_query, name='api_edge_query'),
    path('edgemanage', views.api_edge_conf, name='api_edge_conf'),
]
