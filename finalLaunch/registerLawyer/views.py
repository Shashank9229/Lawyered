from django.shortcuts import render
from .forms import  lawyerRegisterForm
from .models import LawyerRegisterDetail

# Create your views here.
def lawyerRegisterView(request):
	if request.method=='POST':
		reg_form=lawyerRegisterForm(request.POST)
		if reg_form.is_valid():
			print("xxxxxxxxxxxxxxxxxxxxxx")

			reg_obj=reg_form.save()
			reg_obj.save()
			return render(request,'registerLawyer/registerThankyou.html',{'reg_obj':reg_obj})
		
		else:
			print(reg_form.errors)
			
	if request.method=='GET':
		reg_form=lawyerRegisterForm()
	return render(request,'registerLawyer/registerBlock.html',{'reg_form':reg_form})

def lawyerThankView(request):
	if request.method=='GET':
		return render(request,'registerLawyer/registerThankyou.html')
