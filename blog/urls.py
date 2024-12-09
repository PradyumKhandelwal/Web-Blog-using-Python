from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('create', views.post_create, name='create'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    # path('Registration', views.User_registration1, name='registr'),
]
