from rest_framework.routers import DefaultRouter
from .views import ArticleViewSets

router = DefaultRouter()
router.register('articles', ArticleViewSets,  basename='article')

urlpatterns = router.urls
