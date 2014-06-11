from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):

    list_filter = ('answered', )
    list_display = ('fio', 'contact', 'create_date', 'answered')


admin.site.register(Question, QuestionAdmin)
