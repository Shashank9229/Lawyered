from datetime import datetime
from django.core.urlresolvers import reverse
from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField


class Article(models.Model):
	article_title=models.CharField('Enter the title of your article',max_length=200,unique=True)
	article_slug=models.SlugField(max_length=100,unique=True)
	article_body=models.TextField('Enter the body of article',)
	cover_image=models.ImageField(upload_to='blogHone/articleImages')
	article_author=models.CharField('Enter author name',max_length=100)
	pub_date=models.DateTimeField('date published',default=datetime.now,blank=True)
	def get_absolute_url(self):
		return reverse('blogHome.views.',args=[str(self.article_slug)])
	def __str__(self):
		return self.article_title		

class InterestedPeople(models.Model):
	person_name=models.CharField(max_length=100,blank=False)
	person_email=models.EmailField(blank=False)
	person_city=models.CharField(max_length=30)
	phone_number=models.CharField(unique=True,max_length=14)
	def __str__(self):
		return self.person_name


