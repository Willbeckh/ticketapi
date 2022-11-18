from django.contrib.auth.models import User
from .serializers import Register
from rest_framework.permissions import AllowAny
from rest_framework import generics

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = Register