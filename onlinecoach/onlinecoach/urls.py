from django.contrib import admin
from django.urls import include, path
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('q/', include('qa.urls')),
    path('u/', include('user.urls')),
    path('', home_views.index)
]
