from django.shortcuts import render_to_response
from django.contrib import auth

def index(request):
	if request.user.is_authenticated():
		username = request.user.username
	else:
		return render_to_response('news/base_news.html', {'is_auth': False})
	return render_to_response('news/base_news.html', {'is_auth': True, 'username': username})