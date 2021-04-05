from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

router = DefaultRouter()
router.register(r"", CommentViewSet, "comment")

urlpatterns = router.urls
