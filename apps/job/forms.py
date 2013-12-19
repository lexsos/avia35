from django import forms

from .models import VacancyResponse



class ResponseForm(forms.ModelForm):
    class Meta:
        model = VacancyResponse
        fields = ('fio', 'phone', 'about_self', 'summary')
