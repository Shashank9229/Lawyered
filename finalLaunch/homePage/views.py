from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.template.context_processors import csrf
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.contrib import messages
from .models import EmailId
from .forms import EmailForm
import json


all_email_objects=EmailId.objects.all()
all_email_list=[x.email_id for x in all_email_objects]
user_email=None


def homeView(request):
	if request.method=='GET':
		email_form=EmailForm()
	return render(request,'homePage/emailForm.html',{'email_form':email_form})


def ajaxHomeView(request):
	if request.method=='POST' and request.is_ajax():
		user_email=request.POST.get('posted_email')
		response_data={}

		if user_email in all_email_list:
			response_data['result']='duplicate'
			return JsonResponse(response_data)
			
		else:
			email=EmailId(email_id=user_email)
			response_data['result']='success'
			messages.success(request,'THANK You for Joining')
			email.save()
			return JsonResponse(response_data)

	else:
		return HttpResponse(
				json.dumps({"xx":"not"}),content_type="application/json"
			)	




