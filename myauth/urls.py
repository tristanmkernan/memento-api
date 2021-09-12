from django.urls import path, include
from rest_framework import routers

from .views import AuthenticationViewSet

router = routers.DefaultRouter()

router.register("myauth", AuthenticationViewSet, basename="myauth")

urlpatterns = [
    path("", include(router.urls))
]
