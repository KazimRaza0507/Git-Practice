from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    path('token', ObtainAuthToken.as_view(), name='token'),
]