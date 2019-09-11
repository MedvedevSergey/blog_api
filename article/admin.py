from django.contrib import admin
from .models import Article, Tag

admin.site.register([Tag])


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    filter_horizontal = ['tags']

