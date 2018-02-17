from django.urls import resolve

from core.models import PageContent


def additional_page_content(request):
    url_name = resolve(request.path_info).url_name
    return dict(additional_content=PageContent.get_content(url_name))
