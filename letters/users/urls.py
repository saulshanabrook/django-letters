from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^user/(?P<slug>\w+/)$', DetailView.as_view(model=User)),
)
