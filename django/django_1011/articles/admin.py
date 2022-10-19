from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # Admin계정으로 접속했을 시 보이는 항목들
    list_display = ('title', 'user', 'created_at', 'updated_at')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'content')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
