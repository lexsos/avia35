from django.views.generic import FormView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from .forms import ResponseForm
from .models import Vacancy


class AddResponse(FormView):

    form_class = ResponseForm
    template_name = 'job/response_form.html'

    def dispatch(self, *args, **kwargs):
        vacancy_id = self.kwargs['pk']
        self.vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
        return super(AddResponse, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.vacancy = self.vacancy
        instance.save()
        return super(AddResponse, self).form_valid(form)

    def get_success_url(self):
        return reverse('job_response_success')

    def get_context_data(self, **kwargs):
        context = super(AddResponse, self).get_context_data(**kwargs)
        context['vacancy'] = self.vacancy
        return context
