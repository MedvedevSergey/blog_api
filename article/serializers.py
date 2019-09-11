from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Article, Tag


class TagSerializer(ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializer(ModelSerializer):
    tags = TagSerializer(many=True)
    comment_count = IntegerField()

    class Meta:
        model = Article
        fields = '__all__'
