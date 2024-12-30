from django.test import TestCase
from .models import TODO

class TodoTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        TODO.objects.create(title = 'First TODO Title', body = "Todo body here")

    
    def test_title_content(self):
        todo = TODO.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, 'First TODO Title')
    
    def test_body_content(self):
        todo = TODO.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEqual(expected_object_name, 'Todo body here')