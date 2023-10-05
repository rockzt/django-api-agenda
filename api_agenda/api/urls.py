from django.urls import path, include
from rest_framework import routers
from . import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Following REST FRAMEWORK best practices

router = routers.DefaultRouter()
router.register(r'contacts', viewsets.ContactViewSet)  # Registering viewset
router.register(r'users', viewsets.UserViewSet, basename="user")  # Registering viewset


urlpatterns = [
    path('api/', include(router.urls)),  # Setting urls registered on router on "api/"
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh")
]