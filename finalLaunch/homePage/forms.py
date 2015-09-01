from django import forms
from .models import EmailId

class EmailForm(forms.ModelForm):
	class Meta:
		model=EmailId
		fields=('email_id',)
		widgets={
			'email_id':forms.TextInput(
					attrs={'placeholder':'Email me when it\'s ready','type':'email','class':'form-control'}
				)
		}
		

		