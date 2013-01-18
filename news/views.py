from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext

def index(request):
	return render_to_response('news/base_news.html', context_instance = RequestContext(request))