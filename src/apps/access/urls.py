from django.urls import path

from apps.access.views import AccessRequestView

urlpatterns = [
    path('request/', AccessRequestView.as_view(), name='access-request'),
]
