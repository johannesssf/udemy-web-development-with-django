from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=120)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        email_content = f"Nome: {name}\nE-mail: {email}\nAssunto: {subject}\nMensagem: {message}"
        mail = EmailMessage(
            subject=subject,
            body=email_content,
            from_email='django-intermediate.com',
            to=['myclient@gmail.com'],
            headers={'Reply-To': email}
        )
        mail.send()
