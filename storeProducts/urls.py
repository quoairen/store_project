from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path("", views.index, name='index'),
    path("products/", views.products_list, name='products'),  # /products/
    path('<int:pk>/', views.product_detail, name='product_detail'),  # detail page
]
