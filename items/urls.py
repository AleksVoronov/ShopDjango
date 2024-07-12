from django.urls import path
from items import views

app_name = 'items'

urlpatterns = [

    path('<slug:category_slug>/', views.catalog, name='index'),
    #path('<slug:category_slug>/<int:page>/', views.catalog, name='index'),
    path('products/<slug:product_slug>/', views.products, name='products'),
]