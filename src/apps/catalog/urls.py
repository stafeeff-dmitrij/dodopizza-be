from django.urls import path

from apps.catalog.views import CategoryListView

urlpatterns = [
    path('categories/', CategoryListView.as_view({'get': 'list'}), name='categories'),

]
