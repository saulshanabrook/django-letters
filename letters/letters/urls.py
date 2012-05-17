from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^letter/(?P<year>\d{4})/(?P<month>\d{2})/(?P<title>\w+)/$',
        LetterDetailView.as_view()),
)