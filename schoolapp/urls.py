from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('blog/', views.Blog.as_view(), name='blog'),
    path('detailpage/<int:pk>', views.DetailPage.as_view(), name='detailpage'),
]
