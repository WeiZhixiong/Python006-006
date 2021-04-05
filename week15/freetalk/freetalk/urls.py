from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
# from rest_framework import urls


api_v1 = [
    path('users/', include('users.urls')),
    path('aritcle/', include('article.urls')),
    path('comment/', include('comment.urls'))
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title='free talk')),
    path('api/v1/', include(api_v1))
]
