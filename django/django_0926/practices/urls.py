from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('ping/', views.ping),
    path('pong/', views.pong),
    path('nct/', views.nct),
    path('nctmatch/', views.nctmatch),
    path('is_odd_even/<int:number>', views.is_odd_even),
    path('calculate/<int:n1>/<int:n2>', views.calculate),
    path('lorem/', views.lorem),
    path('lorem_result/', views.lorem_result),
]