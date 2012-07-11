from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

from .models import Letter


class LetterDetailView(DetailView):
    def get_object(self):
        return get_object_or_404(Letter,
                                 date_time_created__year=self.kwargs['year'],
                                 date_time_created__month=self.kwargs['month'],
                                 title=self.kwargs['title'],)
