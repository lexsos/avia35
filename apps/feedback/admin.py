from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):

    list_display = ('fio', 'contact', 'create_date')


admin.site.register(Question, QuestionAdmin)
