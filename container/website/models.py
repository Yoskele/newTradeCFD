from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Article(models.Model):
    ARTICLE_POSTION = (
        ('F', 'forex'),
        ('C', 'commodities'),
        ('G', 'guest_post'),
        ('B', 'broker'),
    )
    slug = models.SlugField()
    article_name = models.CharField(max_length=100, unique=True)
    meta_title = models.CharField(max_length=500, blank=True)
    meta_description = models.TextField(max_length=500, blank=True)
    article_title = models.CharField(max_length=100, blank=True)
    content = RichTextUploadingField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='article', blank=True)
    ticket_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=1, choices=ARTICLE_POSTION)


