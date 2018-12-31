import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls import reverse

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

def create_question(question_text, days):
    '''Create A Question With Text Of question_text and published days number of days in past/future'''
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        '''If no questions, display message'''
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are avaialble right now.')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        '''if past question, display index page'''
        create_question(question_text="Past question?", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question?>'])

    def test_future_question(self):
        '''if future question, display no questions found'''
        create_question(question_text='Future question?', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are avaialble right now.')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        '''if a future and a past question, only display past question'''
        create_question(question_text="Past question?", days=-30)
        create_question(question_text='Future question?', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question?>'])

    def test_two_past_questions(self):
        '''index page will display multiple question'''
        create_question(question_text="Past question?", days=-30)
        create_question(question_text="Another past question?", days=-60)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question?>', '<Question: Another past question?>']
        )

