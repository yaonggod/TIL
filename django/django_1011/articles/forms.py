from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image', 'thumbnail']
        labels = {'title':'제목', 'content':'내용', 'image':'사진', 'thumbnail':'썸네일'}
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'image']
        labels = {'content':'', 'image':'사진'}