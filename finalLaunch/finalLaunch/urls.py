"""finalLaunch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,static
from django.conf import settings
from django.contrib import admin
from homePage.views import homeView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','homePage.views.homeView',name='homeView'),
    url(r'^register/$','homePage.views.ajaxHomeView',name='ajaxHomeView'),
    url(r'^legal-disrupt/$','blogHome.views.ldHomeView',name='ldHomeView'),
    url(r'^legal-disrupt/articles/(?P<slug>[^\.]+)/$','blogHome.views.singleArticleView',name='singleArticleView'),
    url(r'^lawyer-registration/$','registerLawyer.views.lawyerRegisterView',name='lawyerRegisterView'),
    url(r'^thank-you/$','registerLawyer.views.lawyerThankView',name='lawyerThankView'),
    url(r'^legal-disrupt/articles/$','blogHome.views.allArticleView',name='allArticleView'),

]+ static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404='blogHome.views.handler404'

 
