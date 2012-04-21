from django.views.generic import DetailView
from letters.models import Letter


class LetterDetailView(DetailView):
    def get_object(self):
        return get_object_or_404(Space,
                                 date_time_created__year='year',
                                 date_time_created__month='month',
                                 title='title',)