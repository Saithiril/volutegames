from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.template import RequestContext
from VoluteGames.forms import RegistrationForm

def logout(request):
	if request.user.is_active:
		auth.logout(request)
	# return render_to_response('news/base_news.html')
	return HttpResponseRedirect("home")

def login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('home')
	else:
		return render_to_response('auth.html', {'error': True,}, context_instance = RequestContext(request))

def authorization(request):
	return render_to_response('auth.html', {'error': False,}, context_instance = RequestContext(request))
	
def registration(request):
	form = RegistrationForm()
	return render_to_response('registration.html', {'form': form}, context_instance = RequestContext(request))
	
def signup(request):
	username = request.POST['subject']
	password = request.POST['password']
	confirm = request.POST['re_password']
	mail = request.POST['email']
	form = RegistrationForm({'subject': username, 'password': password, 're_password': confirm, 'email': mail})
	if password==confirm:
		if form.is_valid():
			try:
				user = User.objects.get(username=username)
				form['subject'].className = 'short_test'
			except (User.DoesNotExist):
				pass
				user = User.objects.create_user(username=form.cleaned_data['subject'], email=form.cleaned_data['email'], password=password)
				user.is_staff = False
				user.save()
				return HttpResponseRedirect('home')
	return render_to_response('registration.html', {'form': form}, context_instance = RequestContext(request))