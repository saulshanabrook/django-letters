from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView

from .models import User


urlpatterns = patterns('',
    url(r'^user/(?P<slug>\w+/)$', DetailView.as_view(model=User)),
)
