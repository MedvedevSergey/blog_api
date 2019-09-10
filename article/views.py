from rest_framework.viewsets import ModelViewSet
from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSets(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(published=True)



