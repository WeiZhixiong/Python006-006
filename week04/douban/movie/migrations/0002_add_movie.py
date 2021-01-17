# -*- coding: utf-8 -*-

from django.db import migrations

movie_name = "疯狂原始人2"
movie_rating = 8.0


def movie_init_data(apps, schema_editor):
    Movie = apps.get_model("movie", "Movie")
    movie_entity = Movie(
        movie_name=movie_name,
        movie_rating=movie_rating
    )
    movie_entity.save()


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(movie_init_data),
    ]
