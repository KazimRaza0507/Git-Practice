from django.contrib.auth.models import User
from .serializer import RegistrationSerializer
from rest_framework.generics import CreateAPIView
from AuthToken.authentication import ExpireAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class RegisteredUsers(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [ExpireAuthentication]
    permission_classes = [IsAuthenticated]


def deleteuser(request):
    user = User.objects.filter(username='kazim1')
    user.delete()