from django import forms

from job.models import VacancyResponse


class ResponseForm(forms.ModelForm):

    fio = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'как к Вам обращаться', 'class': 'input-xlarge'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'введите номер телефона'}))

    class Meta:
        model = VacancyResponse
        fields = ('fio', 'phone', 'about_self', 'summary')
