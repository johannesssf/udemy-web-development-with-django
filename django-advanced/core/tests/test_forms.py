from django.test import TestCase

from core.forms import ContactForm


class ContactFormTestCase(TestCase):

    def setUp(self):
        self.name = 'Homer Simpson'
        self.email = 'homer@gmail.com'
        self.subject = 'Some subject'
        self.message = 'The message content'

        self.data = {
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message,
        }

        self.form = ContactForm(data=self.data) # ContactForm(request.POST)

    def test_send_mail(self):
        form1 = ContactForm(data=self.data)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)
