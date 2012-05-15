from django.test import TestCase
from django.contrib.admin.models import User

from letters.models import Letter

user.get_profile()
class AnimalTestCase(TestCase):
    def setUp(self):
        self.user_one = User.objects.create(username='testusername_one')
        self.user_two = User.objects.create(username='testusername_two')
        self.user_three = User.objects.create(username='testusername_three')
        self.letter = Letter.objects.creat(title='letter_title',
                    content='letter_content', author=self.user_one

    def test_user_(self):
        """Animals that can speak are correctly identified"""
        self.assertEqual(self.lion.speak(), 'The lion says "roar"')
        self.assertEqual(self.cat.speak(), 'The cat says "meow"')