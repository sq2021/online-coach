from django.urls import path

from . import views

app_name = 'qa'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.view, name='question'),
    path('<int:pk>/update', views.QuestionUpdateView.as_view(), name='Question Update'),
    path('new', views.QuestionNewView.as_view(), name='Question Creation')
]