from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import generics, mixins, status

from apps.catalog.models import Ingredient, Product
from apps.catalog.serializers.ingredient import IngredientProductSerializer
from config.settings import CACHE_TIMEOUT


@extend_schema(tags=['Каталог'])
@method_decorator(cache_page(CACHE_TIMEOUT), name='dispatch')
class IngredientsListView(generics.GenericAPIView, mixins.ListModelMixin):
    """
    Возврат ингредиентов
    """

    serializer_class = IngredientProductSerializer
    pagination_class = None

    def get_queryset(self) -> list[Product]:
        """
        Фильтрация ингредиентов по категории
        """
        category_id = self.request.query_params.get('category_id')

        if category_id:
            ingredients = Ingredient.objects.filter(category_id=category_id)
        else:
            ingredients = Ingredient.objects.all()

        return ingredients.filter(status=True).order_by('order')

    @extend_schema(
        summary='Возврат ингредиентов',
        description='Возврат ингредиентов с возможностью фильтрации по id категории',
        parameters=[
            OpenApiParameter(name='category_id', description='id категории', required=False, type=int),
        ],
        responses={
            status.HTTP_200_OK: IngredientProductSerializer,
        }
    )
    def get(self, request):
        return self.list(request)
