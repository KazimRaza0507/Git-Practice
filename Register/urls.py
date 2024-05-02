from django.urls import path
from .views import RegisteredUsers, deleteuser

urlpatterns = [
    path('create_user', RegisteredUsers.as_view()),
    path('delete/', deleteuser)
]