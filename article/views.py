from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Article
from .serializers import ArticleSerializer
from comment.serializers import CommentSerializer


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(published=True)

    @action(detail=True, methods=['get'])
    def comments(self, request, *args, **kwargs):
        article = self.get_object()
        serializer = CommentSerializer(article.comments.all(), many=True, context=self.get_serializer_context())
        return Response(serializer.data)
