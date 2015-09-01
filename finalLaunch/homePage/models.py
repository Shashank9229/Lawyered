from datetime import datetime
from django.db import models
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

HTML_MESSAGE='<!DOCTYPE html> <html> <body> <table style="width:100%;color: #333333;overflow:hidden;border-collapse:collapse;"> <tbody> <tr style="text-align:center; vertical-align:middle;background-color:black;"> <img style="width:100%;" src="https://s3-ap-northeast-1.amazonaws.com/teamlawyered/Screen+Shot+2015-08-27+at+5.58.44+pm.png" > </tr> </tbody> </table> </body> </html> '
# Create your models here.

class EmailId(models.Model):
	email_id=models.EmailField()
	date=models.DateTimeField(default=datetime.now,blank=True)
	def __str__(self):
		return self.email_id + " registered at " +self.date.strftime("%Y-%m-%d")
	
	def save(self):
		if self.email_id:
			send_mail('subject','','ordbms1@gmail.com',[self.email_id],fail_silently=True,html_message=HTML_MESSAGE)
		super(EmailId,self).save()	
