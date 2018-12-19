import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_wtih_future_question(self):
        '''If date is in the future, was_publised recently() should return False'''
        time = timezone.now() + datetime.timedelta(weeks=1664)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_wtih_old_question(self):
        ''' if date is older than one day, was published recently should return false'''
        time = timezone.now() - datetime.timedelta(days = 1, seconds =1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_wtih_recent_question(self):
        '''if date is within the past day, was_published_recently() should return True'''
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59, milliseconds=999)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    


