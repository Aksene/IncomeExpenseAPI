"""incomeexpensesapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# SWAGGER UI
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Income Expense API",
#       default_version='v1',
#       description="An API for income expenses",
#       terms_of_service="https://www.yourco.com/terms/",
#       contact=openapi.Contact(email="contact@income.remote"),
#       license=openapi.License(name="Test License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

# The first thing to get called
urlpatterns = [
    path('admin/', admin.site.urls),
    # Sends them to urls.py in authentication
    path('auth/', include('authentication.urls')),
    # path('', schema_view.with_ui('swagger', 
    #                                 cache_timeout=0), name='schema-swagger-ui'),
    # path("redoc", schema_view.with_ui('redoc', 
    #                                     cache_timeout=0), name='schema-redoc'),
]
