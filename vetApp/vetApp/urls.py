"""vetApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from pets.views import (
    AdminPetOwnerViewSet,
    AdminPetViewSet,
    PetOwnerViewSet,
    PetViewSet,
)
from vetApp.router import router

router.register("pet-owners", PetOwnerViewSet)
router.register("pets", PetViewSet)
router.register("admin-pet-owners", AdminPetOwnerViewSet, basename="admin-pet-owners")
router.register("admin-pets", AdminPetViewSet, basename="admin-pets")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + [
        path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    ]
