from django.urls import path
from .views import (
    ProductList, ProductDetail, ProductCreate, ProductUpdate, ProductDelete
)


urlpatterns = [
    path('products/', ProductList.as_view(),name='products'),
    path('product/<int:pk>/', ProductDetail.as_view(),name='product'),
    path('product/create/', ProductCreate.as_view(),name='product-create'),
    path('product/update/<int:pk>/', ProductUpdate.as_view(),name='product-update'),
    path('product/delete/<int:pk>/', ProductDelete.as_view(),name='product-delete'),
]