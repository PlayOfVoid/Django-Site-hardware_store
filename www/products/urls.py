
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('',views.index,name='index'),
    path('catalog/',views.catalog,name='catalog'),
    path('category/<int:category_id>/',views.category,name='category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # Подробное описание товара
   

    ]
