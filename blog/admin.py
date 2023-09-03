from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body',)
    list_filter = ('title',)
    search_fields = ('title', 'body',)
