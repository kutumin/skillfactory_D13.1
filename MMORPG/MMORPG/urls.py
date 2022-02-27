from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.flatpages import views
from .views import PostListNews, PostAdd, IndexView
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', lambda request: redirect('info/', permanent=False)),
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('blog/', PostListNews.as_view()),
    path('add/', PostAdd.as_view()),
    path('accounts/', include('allauth.urls')),
    path('protect/', IndexView.as_view()),
]
