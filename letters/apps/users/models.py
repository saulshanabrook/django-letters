from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify

from ..posts.models import Letter


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    slug = models.SlugField()

    def last_letter_recipients(self):
        """Return the last users shared to in a letter"""
        try:
            return self.letter_set.latest().shared_with
        except 'DoesNotExist':
            return None

    def all_letters_recipients(self):
        """Return all the users that user has shared letters with"""
        return self.letter_set.values_list('user_shared_with', flat=True)

    def last_comment_recipients(self, Letter):
        """Return users shared in last comment by author in letter."""
        return Letter.comment_set.filter(author=self).latest().shared_with


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
