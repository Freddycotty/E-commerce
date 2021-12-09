from django.urls import path
from .views import all_products, product_detail
app_name = 'store'

urlpatterns = [
    path('', all_products, name = 'all_products'),
    path("item/<slug:slug>/", product_detail, name="product_detail")
]
