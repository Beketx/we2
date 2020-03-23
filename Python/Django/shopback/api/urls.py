from django.urls import path
from api.views import*
urlpatterns = [
    path('products/',product_list),
    path('products/<int:product_id>/',product_detail),
    path('categories/',category_list),
    path('categories/<str:category_name>/',category_detail),
    path('categories/<str:category_name>/products/',category_product)
]