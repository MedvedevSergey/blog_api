from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    published_datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='article/', blank=True, null=True)
    author = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['published_datetime', 'title']


class Tag(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
