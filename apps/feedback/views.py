from django.views.generic import FormView
from django.urls import reverse

from feedback.forms import QuestionForm
from feedback.utils import send_question_notice


class AddQuestion(FormView):

    form_class = QuestionForm
    template_name = 'feedback/question_form.html'

    def get_success_url(self):
        return reverse('feedback_question_success')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        send_question_notice(instance)
        return super(AddQuestion, self).form_valid(form)
