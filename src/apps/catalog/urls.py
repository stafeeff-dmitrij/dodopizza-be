from django.urls import include, path

from apps.catalog.views.category import CategoryListView
from apps.catalog.views.product import (
    AllProductsListView,
    ProductDetailView,
    ProductsFilterListView,
)

urlpatterns = [
    path('categories/', CategoryListView.as_view({'get': 'list'}), name='categories'),
    path('all_products/', AllProductsListView.as_view({'get': 'list'}), name='all_products'),

    path('products/', include([
        path('', ProductsFilterListView.as_view(), name='products'),
        path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    ])),
]
