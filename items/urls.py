from django.urls import path
from items import views

app_name = 'items'

urlpatterns = [
    path('search/', views.catalog, name='search'),
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('products/<slug:product_slug>/', views.products, name='products'),
]