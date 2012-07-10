from django.db import models

from lettters.users.models import User


class Letter(models.Model):
    title = models.CharField(
        max_length=60,
        unique_for_month="date_time_created")
    content = models.TextField()
    author = models.ForeignKey(
        User,
        editable=False)
    show_author = models.BooleanField(
        default=True,
        verbose_name='Show the author?')
    date_time_created = models.DateTimeField(
        auto_now_add=True)
    users_shared_with = models.ManytoManyField(
        User,
        default=author.last_letter_shared_with(),
        verbose_name='Shared with')

    class Meta:
        get_latest_by = 'date_time_created'
        ordering = ['-date_time_created']

    def __unicode__(self):
        return u'{} by {} at {}'.format(self.title,
                                        self.author,
                                        self.date_time_created)
