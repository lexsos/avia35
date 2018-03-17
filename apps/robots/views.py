from django.template.response import TemplateResponse
from django.contrib.sites.models import Site
from django.http import Http404

from robots.models import RobotData


def robots_txt(request):
    data_list = RobotData.objects.published().filter(site=Site.objects.get_current())
    if data_list.count() == 0:
        raise Http404
    context = {'robotdata_list': data_list}
    return TemplateResponse(request, 'robots/robotdata_list.txt', context, content_type='text/plain')
