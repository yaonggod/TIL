from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:pk>', views.detail, name='detail'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    path('delete/', views.delete, name='delete'),
    path('<int:pk>/follow/', views.follow, name='follow'),
]