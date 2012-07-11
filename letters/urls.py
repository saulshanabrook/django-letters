from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< Updated upstream
from django.views.generic import TextView
=======
>>>>>>> Stashed changes


urlpatterns = patterns('',
    url(r'^robots\.txt$', TextView.as_view(template_name="robots.txt")),
    url(r'^humans\.txt$', TextView.as_view(template_name="humans.txt")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
