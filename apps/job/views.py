from django.views.generic import FormView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from dj_mixin.publications.views import PublicationListView

from .forms import ResponseForm
from .models import Vacancy, Note
from .utils import send_response_notice


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
        send_response_notice(instance)
        return super(AddResponse, self).form_valid(form)

    def get_success_url(self):
        return reverse('job_response_success')

    def get_context_data(self, **kwargs):
        context = super(AddResponse, self).get_context_data(**kwargs)
        context['vacancy'] = self.vacancy
        return context


class VacancyListView(PublicationListView):

    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super(VacancyListView, self).get_context_data(**kwargs)
        context['note_list'] = Note.objects.published()
        return context
