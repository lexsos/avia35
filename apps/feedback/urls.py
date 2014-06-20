from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import AddQuestion


urlpatterns = patterns(
    '',
    url(
        r'^$',
        AddQuestion.as_view(),
        name='feedback_add_question',
    ),
    url(
        r'^success/$',
        TemplateView.as_view(template_name="feedback/question_success.html"),
        name='feedback_question_success',
    ),
)
