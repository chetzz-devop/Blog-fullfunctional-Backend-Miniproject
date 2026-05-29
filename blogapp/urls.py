from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('blog/', views.displaypage, name='displaypage'),
    path('readmore/<int:id>/', views.readmore, name='readmore'),
    path('createblog/', views.CreateBlog.as_view(), name='createblog'),
    path('editblog/<int:pk>/', views.editblog.as_view(), name='editblog'),
    path('deleteblog/<int:pk>/', views.Deleteblog.as_view(), name='deleteblog'),
    path('fav/', views.favblog, name='favblog'),
    path('delfav/<int:pk>/', views.deletefav.as_view(), name='deletefav'),

]
