import datetime

from django.test import TestCase
from django.contrib.admin.models import User

from letters.models import Letter


class AnimalTestCase(TestCase):
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

    def tearDown(self):
        self.user_one.delete()
        self.user_two.delete()
        self.user_three.delete()
        self.letter_one.delete()
        self.letter_two.delete()

    def test_user_slug(self):
        from django.template.defaultfilters import slugify
        self.assertEqual(self.user_one.slug, slugify(self.user_one.username))

    def test_last_letter_recipients(self):
        self.assertEqual(self.user_two.last_letter_recipients, None)
        self.assertEqual(self.user_one.last_letter_recipients, [self.user_two])

    def test_all_letter_recipients(self):
        self.assertEqual(self.user_two.all_letters_recipients, None)
        self.assertEqual(self.user_one.all_letters_recipients,
                         [self.user_two, self.user_three])
