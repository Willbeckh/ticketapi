from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from tickets.models import Ticket, Category
from rest_framework import routers
from tickets.views import *

# provides automatic dertermination of the URL conf
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/tickets', TicketViewSet)
router.register(r'api/category', CategoryViewSet, basename='Category')

# wire up paths to router for automatic routing.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('auth.urls')),
]
