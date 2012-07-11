from django.db import models

from ..users.models import User


class Letter(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    author = models.ForeignKey(User, editable=False,
                               related_name='authored_letters')
    show_author = models.BooleanField(
        default=True,
        verbose_name='Show the author?')
    created = models.DateTimeField(auto_now_add=True)
    shared_with = models.ManyToManyField(User,
                                         related_name='addressed_to_letters')

    class Meta:
        get_latest_by = 'created'
        ordering = ['-created']

    def __unicode__(self):
        return u'{} by {} at {}'.format(self.title, self.author,
                                        self.date_time_created)
