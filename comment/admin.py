from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created_at', 'updated_at', 'parent']
    list_display_links = ['id', 'author']
