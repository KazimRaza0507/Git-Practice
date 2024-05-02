from django.urls import path
from .views import GetToken
# from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    path('token', GetToken.as_view(), name='token'),
]