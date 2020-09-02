from django.urls import path, include
from rest_framework import routers

from . import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('edgemanage/<str:dnet>', views.api_edge_query, name='api_edge_query'),
    path('edgemanage', views.api_edge_conf, name='api_edge_conf'),
]
