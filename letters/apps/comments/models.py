from django.db import models

from letters.posts.models import Letter
from letters.users.models import User


class Comment(models.model):
    letter = models.ForeignKey(Letter, editable=False)
    content = models.TextField()
    author = models.ForeignKey(User, editable=False)
    date_time_created = models.DateTimeField(auto_now_add=True)
    shared_with = models.ManytoManyField(User, verbose_name='Shared with')

    class Meta:
        get_latest_by = 'date_time_created'
        ordering = ['-date_time_created']

    def __unicode__(self):
        return u'{}\'s comment on "{}" at {}'.format(self.author,
                                                     self.letter,
                                                     self.date_time_created)
