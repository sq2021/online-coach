from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from home import views as home_views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('q/', include('qa.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('', home_views.index, name='home-index')
]
