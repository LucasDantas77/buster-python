from django.shortcuts import render
from rest_framework.views import APIView, Response, Request, status
from users.models import User
from django.shortcuts import get_object_or_404
from users.permissions import UserAuth
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from users.serializer import UserSerializer


class UserApi(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserApiId(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, UserAuth]

    def get(self, request: Request, id: int) -> Response:
        user = get_object_or_404(User, id=id)
        self.check_object_permissions(request, user)
        return Response(UserSerializer(user).data)

    def patch(self, request: Request, id: int) -> Response:
        user = get_object_or_404(User, id=id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
