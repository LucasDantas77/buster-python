from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, Request, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.models import Movie
from movies.permission import IsAdmin, IsAdminAcess
from movies.serializer import MovieOrderSerializer, MovieSerializer
from users.permissions import UserAuthenticate


class MoviesApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MoviesIdAPi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminAcess]

    def get(self, request: Request, id=int) -> Response:
        movie = get_object_or_404(Movie, id=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def delete(self, request: Request, id=int) -> Response:
        movie = get_object_or_404(Movie, id=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieOrderApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [UserAuthenticate]

    def post(self, request: Request, id: int) -> Response:
        movie = get_object_or_404(Movie, id=id)
        serializers = MovieOrderSerializer(data=request.data)
        if serializers.is_valid():
            order = serializers.save(user=request.user, movies=movie)
            return Response(
                MovieOrderSerializer(order).data, status=status.HTTP_201_CREATED
            )
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
