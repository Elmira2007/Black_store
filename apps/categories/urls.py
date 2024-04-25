from django.urls import path
from apps.categories.views import CategoryViewSet, CategoryDetailAPI


urlpatterns = [
    path('api/categories/', CategoryViewSet.as_view(), name='api/categories/'),
    path('api/categories/<int:pk>/', CategoryDetailAPI.as_view(), name="api/category_detail"),
]