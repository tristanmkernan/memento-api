from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from .models import Memento, MementoCategory
from .serializers import MementoCategorySerializer, MementoSerializer
from .filters import MementoCategoryFilter


class MementoViewSet(ModelViewSet):
    queryset = Memento.objects.none()
    serializer_class = MementoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.memento_set

    class Meta:
        model = Memento


class MementoCategoryViewSet(ModelViewSet):
    queryset = MementoCategory.objects.none()
    serializer_class = MementoCategorySerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MementoCategoryFilter

    def get_queryset(self):
        return self.request.user.mementocategory_set

    class Meta:
        model = MementoCategory
