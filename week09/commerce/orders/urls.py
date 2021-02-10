from django.urls import path
from .views import OrdersViewSet

orders_list = OrdersViewSet.as_view({
    'get': 'list'
})

orders_detail = OrdersViewSet.as_view({
    'get': 'retrieve',
})

orders_create = OrdersViewSet.as_view({
    'post': 'create',
})

orders_cancel = OrdersViewSet.as_view({
    'get': 'cancel'
})

urlpatterns = [
    path('', orders_list, name='orders-list'),
    path('<int:pk>', orders_detail, name='orders-detail'),
    path('create', orders_create, name='orders-create'),
    path('<int:pk>/cancel', orders_cancel, name='orders-cancel')
]


