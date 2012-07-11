from django.conf.urls.defaults import patterns, include, url

from .views import LetterDetailView


urlpatterns = patterns('',
    url(r'^letter/(?P<year>\d{4})/(?P<month>\d{2})/(?P<title>\w+)/$',
        LetterDetailView.as_view()),
)
