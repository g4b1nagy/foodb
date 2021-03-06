from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


app_name = 'products'


urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),

    path('batches/', views.BatchList.as_view(), name='batch_list'),
    path('batches/<int:pk>/', views.BatchDetail.as_view(), name='batch_detail'),

    path('products/<int:pk>/batches/', views.product_batches, name='product_batches'),
    path('products/<int:pk>/inventory/', views.product_inventory, name='product_inventory'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
