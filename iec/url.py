from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from .views import (RegistroController)

urlpatterns = [
    path('registro', RegistroController.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('refresh-session', TokenRefreshView.as_view()),
]