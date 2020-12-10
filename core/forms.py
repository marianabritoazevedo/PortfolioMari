from django import forms
from django.core.mail import send_mail
from django.conf import settings
from core.mail import send_mail_template

class ContactMessage(forms.Form):
	name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class':'form-nome', 'type':'text', 'placeholder':'Seu Nome...'}))
	email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'form-email', 'type':'text', 'placeholder':'Seu E-mail...'}))
	assunto = forms.CharField(label='Assunto', widget=forms.TextInput(attrs={'class':'form-assunto', 'type':'text', 'placeholder':'Assunto do e-mail...'}))
	message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'class':'form-text', 'type':'text', 'placeholder':'Sua mensagem...'}))

	def send_mail(self):
		subject = self.cleaned_data['assunto']
		context = {
			'name': self.cleaned_data['name'],
			'email': self.cleaned_data['email'],
			'message': self.cleaned_data['message'],
		}
		template_name = 'core/contact.html'
		send_mail_template(subject, template_name, context, 
			[settings.CONTACT_EMAIL]
		)