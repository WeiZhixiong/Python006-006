from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('docs/', include_docs_urls(title='commerce')),
    path('orders/', include('orders.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
