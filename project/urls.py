from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^job/', include('job.urls')),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^documents/', include('documents.urls')),
    url(r'^avia_park/', include('avia_park.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^services/', include('services.urls')),

    url(r'^$', include('main_page.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
