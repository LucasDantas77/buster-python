from django.urls import path

from users.views import UserApi, UserApiId
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
   path("users/", UserApi.as_view()),
   path("users/<int:id>/", UserApiId.as_view()),
   path("users/login/", TokenObtainPairView.as_view()),
   path("users/login/refresh/", TokenRefreshView.as_view())
]
