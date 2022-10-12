from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # Admin계정으로 접속했을 시 보이는 항목들
    list_display = ('title', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
