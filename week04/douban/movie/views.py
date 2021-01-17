from django.shortcuts import render
from .models import Movie, MovieComment


def index(request):
    movie = Movie.objects.order_by('-movie_id')[0]
    movie_name = movie.movie_name
    movie_id = movie.movie_id
    user_query_dict = request.GET
    query_str = None
    if 'comment' in user_query_dict:
        query_str = user_query_dict["comment"]

    if query_str:
        comment_list = MovieComment.objects.filter(
            movie_id=movie_id,
            comment__contains=query_str
        )[:40]
    else:
        comment_list = MovieComment.objects.filter(
            movie_id=movie_id,
            star__gt=3
        )[:40]

    for comment in comment_list:
        comment.comment = comment.comment.strip("'").replace("\\n", "\n")
    context = {
        "movie_name": movie_name,
        "comment_list": comment_list,
    }
    return render(request, "index.html", context)
