from django.urls import path
from .views import all_products, product_detail, category_list
app_name = 'store'

urlpatterns = [
    path('', all_products, name = 'all_products'),
    path("<slug:slug>/", product_detail, name="product_detail"),
    path("shop/<slug:category_slug>/", category_list, name="category_list"),
]
