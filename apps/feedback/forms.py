from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Question


class QuestionForm(forms.ModelForm):

    fio = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': _('please, enter fio'),
                'class': 'input-xlarge',
            }
        )
    )
    contact = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': _('please, enter contact'),
                'class': 'input-xlarge',
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': _('please, enter question')}
        )
    )

    class Meta:
        model = Question
        fields = ('fio', 'contact', 'content')
