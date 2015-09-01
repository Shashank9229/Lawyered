from django import forms
from .models import InterestedPeople

class ContactForm(forms.ModelForm):
	class Meta:
		model=InterestedPeople
		fields=('person_name','person_email','person_city','phone_number',)
		widgets={
			'person_name':forms.TextInput(
					attrs={'placeholder':'first name','class':'form-control'}
				),
			'person_email':forms.EmailInput(
					attrs={'placeholder':'Enter your email address','class':'form-control'}
				),
			'person_city':forms.TextInput(
					attrs={'placeholder':'Enter City','class':'form-control'}
				),
			'phone_number':forms.NumberInput(
					attrs={'placeholder':'Enter your 10-digit mobile number','class':'form-control'}
				)
		}