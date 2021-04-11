from django.urls import path
from .views import ActiveList

urlpatterns = [
    path('', ActiveList.as_view(), name='active'),
]
