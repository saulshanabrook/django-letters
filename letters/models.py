from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Letter(models.Model):
    title = models.CharField(max_length=60, unique_for_date="date_time_created")
    content = models.TextField()
    author = models.ForeignKey(User, editable=False)
    show_author = models.BooleanField(default=True, verbose_name='Show the author?')
    date_time_created = models.DateTimeField(auto_now_add=True)
    users_shared_with = models.ManytoManyField(User, default=self.author.last_letter_shared_with(), verbose_name='Shared with')

    class Meta:
        get_latest_by = 'date_time_created'
        ordering = ['-date_time_created']

    def __unicode__(self):
        return u'{} by {} at {}'.format(self.title, self.author, self.date_time_created)


class Comment(models.model):
    letter = models.ForeignKey(Letter, editable=False)
    content = models.TextField()
    author = models.ForeignKey(User, editable=False)
    date_time_created = models.DateTimeField(auto_now_add = True)
    shared_with = models.ManytoManyField(User, verbose_name='Shared with')

    class Meta:
        get_latest_by = 'date_time_created'
        ordering = ['-date_time_created']
    
    def __unicode__(self):
        return u'{}\'s comment on "{}" at {}'.format(self.author, self.letter, self.date_time_created)

        
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    def last_letter_shared_with(self):
        """Return the last users with to in a letter"""
        try:
            return self.letter_set.latest().user_shared_with
        except DoesNotExist:
            return None
    
    def all_letter_shared_recipients(self):
        """Return all the users shared letters with"""
        return self.letter_set.values_list('user_shared_with', flat=True)
    
    def last_comment_shared_recipients(self, Letter):
        """Return the last users shared to in the last comment by this user in this letter"""
        return Letter.comment_set.filter(author__exact=self).latest()
    
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        post_save.connect(create_user_profile, sender=User)