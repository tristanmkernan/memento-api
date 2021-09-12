from django.urls import path, include
from rest_framework import routers

from .views import MementoViewSet, MementoCategoryViewSet

router = routers.DefaultRouter()

router.register("mementos", MementoViewSet)
router.register("memento-categories", MementoCategoryViewSet)

urlpatterns = [
    path("", include(router.urls))
]
