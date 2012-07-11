import datetime

from django.utils import unittest
from django.contrib.admin.models import User

from ...posts.models import Letter
from ...comments.models import Comment


class UserTest(unittest.TestCase):
    def tearDown(self):
        self.user_one.delete()
        self.user_two.delete()
        self.user_three.delete()
        self.letter_one.delete()
        self.letter_two.delete()

    def test_last_letter_recipients(self):
        # No letters should return false
        self.assertFalse(self.user_two.last_letter_recipients)
        # Return user(s) shared in last letter
        self.assertEqual(self.user_one.last_letter_recipients, [self.user_two])

    def test_all_letter_recipients(self):
        # No letters should return false
        self.assertFalse(self.user_two.all_letters_recipients)
        # Multiple letters should return list w/ out duplicates
        self.assertEqual(self.user_one.all_letters_recipients,
                         [self.user_two, self.user_three])

    def test_recipients_from_last_comment(self):
        # If this is the first comment, return false
        self.assertFalse(self.user_two.last_comment_recipients(self.letter_one))
        # Return users shared in last comment
        self.assertEqual(self.user_one.last_comment_recipients(self.letter_one),
                         [self.user_two, self.user_three])
