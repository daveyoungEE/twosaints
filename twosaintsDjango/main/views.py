# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from main.models import Announcement
from main.models import Event
from main.models import Blog
from django.http import Http404

def index(request):
	announcements = Announcement.objects.all().order_by('-date')
	blogEntries = Blog.objects.all().order_by('-date')
	return render(request, 'main/index.html',{
		'announcements': announcements,
		'blogEntries': blogEntries,
		})

def announcement_detail(request, id):
	try:
		announcement = Announcement.objects.get(id=id)
	except Announcement.DoesNotExist:
		raise Http(404) ('this announcement does not exist')
	return render(request, 'main/announcement_detail.html', {
			'announcement': announcement,
		})

def blog(request):
	blogEntries = Blog.objects.all().order_by('-date')
	return render(request, 'main/blog.html',{
		'blogEntries': blogEntries,
		})

def blog_detail(request, id):
	try:
		blogEntry = Blog.objects.get(id=id)
	except Blog.DoesNotExsit:
                raise Http(404) ('this blog entry does not exist')
	return render(request, 'main/blog_detail.html', {
			'blogEntry': blogEntry,
		})

def calendar(request):
	events = Event.objects.all().order_by('-date')
	return render(request, 'main/calendar.html',{
		'events': events,
		})

def calendar_detail(request, id):
	try:
		event = Event.objects.get(id=id).order_by('-date')
	except Event.DoesNotExist:
		raise Http(404) ('this event does not exist')
	return render(request, 'main/calendar_detail.html', {
			'event': event,
		})

def archive(request):
	announcements = Announcement.objects.all().order_by('-date')
	return render(request, 'main/archive.html', {
		'announcements': announcements,
		})

def music(request):
	return render(request, 'main/music.html')

def media(request):
	return render(request, 'main/media.html')

def contact(request):
	return render(request, 'main/contact.html')

def children(request):
	return render(request, 'main/children.html')
