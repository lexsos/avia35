from dj_mixin.publications.views import PublicationListView

from .models import Note, PaymentBanner, Flight


class FlightListView(PublicationListView):

    model = Flight

    def get_context_data(self, **kwargs):
        context = super(FlightListView, self).get_context_data(**kwargs)
        context['note_list'] = Note.objects.published()
        context['payment_banner_list'] = PaymentBanner.objects.published()
        return context
