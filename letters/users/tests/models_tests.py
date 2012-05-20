import datetime

from django.test import TestCase
from django.contrib.admin.models import User
from django.template.defaultfilters import slugify

from letters.posts.models import Letter
from letters.comments.models import Comment


class UserTest(TestCase):
    def setUp(self):
        now = datetime.datetime.now()
        pre_now = now - datetime.timedelta(days=1)

        self.user_one = User.objects.create(username='testusername_one')
        self.user_two = User.objects.create(username='testusername_two')
        self.user_three = User.objects.create(username='testusername_three')
        self.letter_one = Letter.objects.create(
            title='letter_title',
            content='letter_content',
            author=self.user_one,
            date_time_created=now,
            users_shared_with=[self.user_two])
        self.letter_two = Letter.objects.create(
            title='letter_title',
            content='letter_content',
            author=self.user_one,
            date_time_created=pre_now,
            users_shared_with=[self.user_three, self.user_two])
        self.comment_one = Comment.objects.create(
            letter=self.letter_one,
            content='comment content',
            author=self.user_one,
            shared_with=[self.user_two, self.user_three]
            )

    def tearDown(self):
        self.user_one.delete()
        self.user_two.delete()
        self.user_three.delete()
        self.letter_one.delete()
        self.letter_two.delete()

    def test_user_slug(self):
        self.assertEqual(self.user_one.slug, slugify(self.user_one.username))

    def test_last_letter_recipients(self):
        # No letters should return false
        self.assertFalse(self.user_two.last_letter_recipients)
        # Return user(s) shared in last letter
        self.assertEqual(self.user_one.last_letter_recipients, [self.user_two])

    def test_all_letter_recipients(self):
        # No letters should return fakse
        self.assertFalse(self.user_two.all_letters_recipients)
        # Multiple letters should return list w/ out duplicates
        self.assertEqual(self.user_one.all_letters_recipients,
                         [self.user_two, self.user_three])

    def test_recipients_from_last_comment(self):
        # If this is the first comment, return false
        self.assertFalse(self.user_two.last_comment_recipients(letter_one))
        # Return users shared in last comment
        self.assertEqeal(self.user_one.last_comment_recipients(letter_one),
                         [self.user_two, self.user_three])
