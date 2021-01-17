# -*- coding: utf-8 -*-

from django.db import migrations
from pathlib import Path
from datetime import datetime, timedelta, timezone

movie_name = "疯狂原始人2"
douban_movie_id = "24298954"
comment_record_file = Path(Path(__file__).parent.parent, f"{douban_movie_id}.csv")


def comment_init_data(apps, schema_editor):
    Movie = apps.get_model("movie", "Movie")
    MovieComment = apps.get_model("movie", "MovieComment")
    movie_entity = Movie.objects.get(movie_name=movie_name)
    movie_id = movie_entity.movie_id
    with open(comment_record_file, "r") as f:
        comment_list = f.readlines()
    for comment_info in comment_list:
        comment_info = comment_info.split(",")
        comment_time = comment_info[0]
        comment_time = datetime.strptime(comment_time, "%Y-%m-%d %H:%M:%S")
        comment_time = comment_time.astimezone(timezone(timedelta(hours=+8)))
        comment_time = comment_time.astimezone(timezone(timedelta(hours=0)))
        comment_star = float(comment_info[1])
        comment_content = comment_info[2].strip("\n")
        comment_entity = MovieComment(
            movie_id=movie_id,
            comment=comment_content,
            star=comment_star,
            create_time=comment_time
        )
        comment_entity.save()


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_add_movie'),
    ]

    operations = [
        migrations.RunPython(comment_init_data),
    ]
