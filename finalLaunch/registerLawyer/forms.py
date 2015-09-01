from django import forms
from django.forms import extras
from .models import LawyerRegisterDetail
GENDER_CHOICES=(('Male','Male'),('Female','Female'),)
class lawyerRegisterForm(forms.ModelForm):
	gender=forms.ChoiceField(choices=GENDER_CHOICES,initial=GENDER_CHOICES[0][0], widget=forms.RadioSelect())
	#date_of_birth= forms.DateField(widget=)
	#date_of_birth=forms.DateField(widget=forms.DateInput())
	class Meta:
		model = LawyerRegisterDetail
		fields='__all__'
		widgets={
			'first_name':forms.TextInput(
					attrs={'placeholder':'First name','type':'text','class':'form-control'}
				),
			'last_name':forms.TextInput(
					attrs={'placeholder':'Last name','type':'text','class':'form-control'}
				),
			'city_name':forms.TextInput(
					attrs={'placeholder':'Choose your city','type':'text','class':'form-control'}
				),
			'company_name':forms.TextInput(
					attrs={'placeholder':'Enter company name','type':'text','class':'form-control'}
				),
			'date_of_birth':extras.SelectDateWidget(
					attrs={'class':'form-control date-picker'},years=range(1905,2016)
				),
			'email':forms.EmailInput(
					attrs={'placeholder':'Enter your email address','type':'email','class':'form-control'}
				),
			'phone_number':forms.NumberInput(
					attrs={'placeholder':'Enter your 10-digit mobile number','type':'number','class':'form-control'}
				),
			'state_bar_no':forms.TextInput(
					attrs={'placeholder':'State Bar where you originally enrolled','type':'text','class':'form-control'}
				),
			'bar_council_no':forms.TextInput(
					attrs={'placeholder':'Bar Council number','type':'text','class':'form-control'}
				)
			

		}
		exclude=['register_time']