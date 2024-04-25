from django.urls import path
from apps.carts.views import CartListAPIView, CartDetailAPIView

urlpatterns = [
    path('api/cart/', CartListAPIView.as_view(), name='cart/list/'),
    path('api/cart/<int:pk>/', CartDetailAPIView.as_view(), name='cart/detail/'),
]