from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.flatpages import views
from .views import PostListNews, PostAdd, ProductUpdateView, PostDeleteView, PostDetail, PostSearch, comment_approve, comment_remove
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


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
    path('home/', PostSearch.as_view()),
    path('comment/<int:comment_id>/delete/', comment_remove, name='comment_remove'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
