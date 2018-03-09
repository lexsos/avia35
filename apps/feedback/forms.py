from django import forms

from feedback.models import Question


class QuestionForm(forms.ModelForm):

    fio = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'как к Вам обращаться', 'class': 'input-xlarge'}))
    contact = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'введите Ваши контакты', 'class': 'input-xlarge'}))
    content = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'введите Ваш вопрос'}))

    class Meta:
        model = Question
        fields = ('fio', 'contact', 'content')
