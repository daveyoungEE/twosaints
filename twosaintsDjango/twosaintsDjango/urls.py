"""twosaintsDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^announcement/(?P<id>\d+)/', views.announcement_detail, name='announcement_detail'),
	url(r'^calendar/', views.calendar, name='calendar'),
	url(r'^calendar/(?P<id>\d+)/', views.calendar_detail, name='calendar_detail'),
	url(r'^archive/', views.archive, name='archive'),
	url(r'^blog/', views.blog, name='blog'),
	url(r'^blog/(?P<id>\d+)/', views.blog_detail, name='blog_detail'),
	url(r'^media/', views.media, name='media'),
	url(r'^music/', views.music, name='music'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^children/', views.children, name='children'),
	url(r'^admin/', admin.site.urls),
]
