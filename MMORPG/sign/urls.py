from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('protect.urls')),
    path('login/', LoginView.as_view(template_name = 'sign/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name = 'sign/logout.html'),name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name = 'sign/signup.html'), name='signup'),
]