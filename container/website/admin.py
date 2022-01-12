from django.contrib import admin

# Register your models here.
from website.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_name', 'created_at']






admin.site.register(Article, ArticleAdmin)



