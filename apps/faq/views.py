from helpers.views import PublicationListView
from faq.models import FrequentlyQuestion
from faq.settings import CONFIG


class FAQListView(PublicationListView):

    model = FrequentlyQuestion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_ref_list'] = context['object_list'].count() > CONFIG['SMALL_FAQ']
        return context
