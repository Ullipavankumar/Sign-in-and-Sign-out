from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('signin/',views.signin2),
    path('signup/',views.signup),
    path('handle_login/', views.handle_login, name='handle_login'),
    path('handle_logout/', views.handle_logout, name='handle_logout'),
    
]