from django.urls import path

from apps.catalog.views.category import CategoryListView
from apps.catalog.views.product import AllProductsListView, ProductsFilterListView

urlpatterns = [
    path('categories/', CategoryListView.as_view({'get': 'list'}), name='categories'),
    path('all_products/', AllProductsListView.as_view({'get': 'list'}), name='all_products'),
    path('products/', ProductsFilterListView.as_view(), name='products'),
]
