from core.models import PageContent
from django.core.urlresolvers import resolve


def additional_page_content(request):
    url_name = resolve(request.path_info).url_name
    return dict(additional_content=PageContent.get_content(url_name))
