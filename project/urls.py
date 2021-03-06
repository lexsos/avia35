from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^job/', include('job.urls')),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^documents/', include('documents.urls')),
    url(r'^avia_park/', include('avia_park.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^services/', include('services.urls')),
    url(r'^faq/', include('faq.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^robots\.txt$', include('robots.urls')),
    url(r'^history/', include('history.urls')),
    url(r'^$', include('main_page.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
