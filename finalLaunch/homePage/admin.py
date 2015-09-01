from django.contrib import admin
from django.core.mail import send_mail,send_mass_mail
from .models import EmailId

# Register your models here.

def send_email(modeladmin,request,queryset):
	rec_list=[]
	for obj in queryset:
		rec_list.append(obj.email_id)

	send_mass_mail((('subject','some message','ordbms1@gmail.com',rec_list),),fail_silently=False)
			
send_email.short_description = "Send emails to selected users"
class EmailIdAdmin(admin.ModelAdmin):
	list_display=['email_id','date']
	actions=[send_email]
	
admin.site.register(EmailId,EmailIdAdmin)	