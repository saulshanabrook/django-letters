from django.views.generic import DetailView
from letters.models import Letter
from django.shortcuts import get_object_or_404


class LetterDetailView(DetailView):
    def get_object(self):
        return get_object_or_404(Letter,
                                 date_time_created__year='year',
                                 date_time_created__month='month',
                                 title='title',)
