from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # path('api/', include('apps.catalog.urls')),

    path('api/', include([
        path('', include('apps.catalog.urls')),
        path('access/', include('apps.access.urls')),
    ])),

    path('admin/', admin.site.urls),
    # Swagger UI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # path('silk/', include('silk.urls', namespace='silk'))  # проверка кол-ва запросов к БД
]

if settings.DEBUG:
    # обслуживание медиа и статических файлов
    urlpatterns.extend(
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    )
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
