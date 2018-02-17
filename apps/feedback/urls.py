from django.conf.urls import url
from django.views.generic import TemplateView

from feedback.views import AddQuestion


urlpatterns = [
    url(r'^add_question/$', AddQuestion.as_view(), name='feedback_add_question'),
    url(r'^success/$', TemplateView.as_view(template_name="feedback/question_success.html"),
        name='feedback_question_success'),
]
