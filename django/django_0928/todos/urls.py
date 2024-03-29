from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:todo_pk>', views.delete, name='delete'),
    path('update/<int:todo_pk>', views.update, name='update'),
    path('detail/<int:todo_pk>', views.detail, name='detail'),
    path('edit/<int:todo_pk>', views.edit, name='edit'),
    path('upload/<int:todo_pk>', views.upload, name='upload')
]