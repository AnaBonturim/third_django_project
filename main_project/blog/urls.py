"""
URL configuration for main_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.LastPostsView.as_view(), name='blog-home'),
    path('posts/', views.AllPostsView.as_view(), name='all-posts'),
    path('posts/<slug:slug>', views.PostView.as_view(), name='post'),
    path('read-later', views.ReadLaterPostView.as_view(), name='read-later'),
    path('read-later/<int:id>', views.RemoveReadLaterView.as_view(), name='read-later-delete'),
    path('comments/', views.AllCommentsView.as_view(), name='all-comments')
]
