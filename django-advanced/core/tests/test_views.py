from django.test import TestCase, Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            'name': 'Homer Simpson',
            'email': 'homer@gmail.com',
            'subject': 'My subject',
            'message': 'My message',
        }
        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.data)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        data = {
            'name': 'Homer Simpson',
            'subject': 'My subject',
        }
        request = self.client.post(reverse_lazy('index'), data=data)
        self.assertEquals(request.status_code, 200)
