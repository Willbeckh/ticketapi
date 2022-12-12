from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from tickets.models import Ticket, Category
from rest_framework import routers
from tickets.views import *


# open api defaults
schema_view = get_schema_view(
    openapi.Info(
        title="Ticket API",
        default_version='v1.0.0',
        description="REST API to create and manage customer tickets ⏯️[open playground on:: https://ticketapi.up.railway.app/sandbox/ ]",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=CustomSchemaGenerator,
)

# provides automatic dertermination of the URL conf
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet, basename="users")
router.register(r'api/tickets', TicketViewSet)
router.register(r'api/category', CategoryViewSet, basename='Category')

# wire up paths to router for automatic routing.
urlpatterns = [
    path('', schema_view.with_ui('redoc',
         cache_timeout=0), name='docs-view'),
    path('sandbox/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-view'),
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('endpoints/', include(router.urls)),
    path('ping/', ping, name="ping"),
]
