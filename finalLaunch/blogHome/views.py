from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import InterestedPeople,Article
from .forms import ContactForm


# Create your views here.
all_articles_obj=Article.objects.all()
all_articles_slugs=[x.article_slug for x in all_articles_obj]


def ldHomeView(request):
	if request.method=='POST':
		form=ContactForm(data=request.POST)
		if form.is_valid():
			interestedPeople_obj=form.save()
			interestedPeople_obj.save()
			return render(request,'blogHome/blogHome.html',{'form':form})
		else:
			print(form.errors)	
	else:
		form=ContactForm()
	all_articles=all_articles_obj
	latest_articles=all_articles[:5]	
	return render(request,'blogHome/blogHome.html',{'form':form,'latest_articles':latest_articles})			

def singleArticleView(request,slug):
	if request.method=='GET':
		if slug in all_articles_slugs:
			current_object=getCurrentObj(slug)
		else:
			return HttpResponse('404 error')
	return render(request,'singleArticle/singleArticle.html',{'current_object':current_object})


def getCurrentObj(slug):
	index_current_slug=all_articles_slugs.index(slug)
	current_object=all_articles_obj[index_current_slug]
	return current_object
	
def allArticleView(request):
	latest_articles3=all_articles_obj[:3]
	return render(request,'allArticles/allArticles.html',{'latest_articles':latest_articles3})

def handler404(request):
	return render(request,'404.html')	