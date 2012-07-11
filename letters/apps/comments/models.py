from django.db import models

from ..posts.models import Letter
from ..users.models import User


class Comment(models.Model):
    letter = models.ForeignKey(Letter, editable=False, related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, editable=False,
                               related_name='authored_comments')
    created = models.DateTimeField(auto_now_add=True)
    shared_with = models.ManyToManyField(User, verbose_name='Shared with',
                                         related_name='addressed_to_comments')

    class Meta:
        get_latest_by = 'created'
        ordering = ['-created']

    def __unicode__(self):
        return u'{}\'s comment on "{}" at {}'.format(self.author, self.letter,
                                                     self.date_time_created)
