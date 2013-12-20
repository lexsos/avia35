from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import VacancyResponse



class ResponseForm(forms.ModelForm):

    fio = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': _('please, enter fio'),
                'class': 'input-xlarge',
            }
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': _('please, enter phone')})
    )

    class Meta:
        model = VacancyResponse
        fields = ('fio', 'phone', 'about_self', 'summary')
