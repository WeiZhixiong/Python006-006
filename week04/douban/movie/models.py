from django.db import models
from django.utils import timezone


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=200, unique=True)
    movie_rating = models.FloatField()

    def __str__(self):
        return self.movie_name


class MovieComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    movie_id = models.IntegerField()
    comment = models.TextField()
    star = models.FloatField()
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment
