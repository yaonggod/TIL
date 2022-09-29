from django.urls import path
from . import views

# 메인(R) - 게시글의 목록(/posts/) / 게시글 상세
# 작성(C) - 글 작성(/posts/new/) / 작성 완료
# 수정(U) - 글 수정 / 수정 완료
# 삭제(D) - 삭제 완료

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name="create"),
    path('delete/<int:pk>', views.delete, name='delete')    
]