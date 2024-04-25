from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer

class CategoryViewSet(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer