from rest_framework.serializers import ModelSerializer
from .models import Article, Tag


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializer(ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = '__all__'
