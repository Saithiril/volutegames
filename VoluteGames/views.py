from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext

def logout(request):
	if request.user.is_active:
		auth.logout(request)
	return render_to_response('news/base_news.html', {'is_auth': False})

def login(request):
	context_instance=RequestContext(request)
	# username = request.POST['username']
	# password = request.POST['password']
	return render_to_response('news/base_news.html', {'is_auth': False}, context_instance)
	# user = auth.authenticate(username=username, password=password)
	# if user is not None and user.is_active:
		# auth.login(request, user)
		# return render_to_response('news/base_news.html', {'is_auth': True, 'username': user.username})
	# else:
		# return render_to_response('news/base_news.html', {'is_auth': False})

def auth(request):
	return render_to_response('auth.html', {'is_auth': False})