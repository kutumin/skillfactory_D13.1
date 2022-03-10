from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.flatpages import views
from .views import PostListNews, PostAdd, IndexView, ProductUpdateView, PostDeleteView, PostDetail
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', lambda request: redirect('info/', permanent=False)),
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/edit', ProductUpdateView.as_view(), name='update_post_detail'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('blog/', PostListNews.as_view()),
    path('add/', PostAdd.as_view()),
    path('accounts/', include('allauth.urls')),
    path('protect/', IndexView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
