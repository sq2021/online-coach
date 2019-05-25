from django.contrib import admin

from .models import Answer, Question
# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ('question_title', 'question_text', 'author' , 'category','is_solved', 'pub_date')
    list_display = ('question_title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_title']
    inlines = [AnswerInline]
admin.site.register(Question, QuestionAdmin)