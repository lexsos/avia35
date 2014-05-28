from dj_mixin.publications.views import PublicationListView

from .models import FrequentlyQuestion
from .settings import CONFIG


class FAQListView(PublicationListView):

    model = FrequentlyQuestion

    def get_context_data(self, **kwargs):
        context = super(FAQListView, self).get_context_data(**kwargs)

        show = context['object_list'].count() > CONFIG['SMALL_FAQ']
        context['show_ref_list'] =  show
        return context
