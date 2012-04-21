from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.generic import Detail
from django.contrib.auth.models import User, Letter


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),

    url(r'^user/(?P<slug>\w+/)$', DetailView.as_view(model=User)),
    url(r'^letter/(?P<year>\d{4})/(?P<month>\d{2})/(?P<title>\w+)/$',
        DetailView.as_view(model=Letter)),

    url(r'^robots\.txt$', TextView.as_view(template_name="robots.txt")),
    url(r'^humans\.txt$', TextView.as_view(template_name="humans.txt")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
