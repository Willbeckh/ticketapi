import requests
from tickets.serializers import *
from rest_framework import viewsets
from tickets.models import Ticket, Category
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.generators import OpenAPISchemaGenerator

# healthchecks ping url
PING_URL = 'https://hc-ping.com/e238b07e-fa0b-425e-8622-d3f12a959b36'


# Create your views here.        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated] # require token authentication.
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    
    
class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = MyTokenObtainPairSerializer
    
# ping endpoint
@api_view(['GET'])
def ping(request):
    """
    This method pings healthchecks.io to verify application liveness.
    """
    try:
        # send a GET request to healthchecks.io
        response = requests.get(PING_URL)

        # check the response
        if response.status_code == 200:
            return Response({ "response" : "Ping Successful!"})
        else:
            return Response(f"Error sending ping: {response.text}")
    except Exception as e:
        print(f"Error sending ping: {str(e)}")
        
        
# swagger schemes generator class
class CustomSchemaGenerator(OpenAPISchemaGenerator):
    """This class overrides the swagger default schema generator class."""
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema
    