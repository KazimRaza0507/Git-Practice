from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.utils import timezone
import pytz
from django.conf import settings


# Create your views here.

class GetToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        utc_now = timezone.now()
        utc_now = utc_now.replace(tzinfo=pytz.utc)
        result = Token.objects.filter(user=user, created__lt=utc_now-settings.DEFAULT_TOKEN_EXPIRY_MINUTES)
        result.delete()
        token,created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})