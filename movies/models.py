from django.db import models


class RatingChoice(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, null=True, default=None)
    rating = models.CharField(
        max_length=20, choices=RatingChoice.choices, default=RatingChoice.G
    )
    synopsis = models.TextField(blank=True, null=True, default=None)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies", null=True
    )


class MovieOrder(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="order_movies",
        null=True,
    )
    
    movies = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="order_movies",
        null=True,
    )
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    



