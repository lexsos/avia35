from django.views.generic import FormView
from django.core.urlresolvers import reverse

from .forms import QuestionForm
from .utils import send_question_notice


class AddQuestion(FormView):

    form_class = QuestionForm
    template_name = 'feedback/question_form.html'

    def get_success_url(self):
        return reverse('feedback_response_success')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        send_question_notice(instance)
        return super(AddQuestion, self).form_valid(form)
