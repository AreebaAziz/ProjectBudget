from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.urls import reverse

from .forms import SignUpForm

@login_required(login_url='/login')
def logout(request):
	auth.logout(request)
	return redirect("index")

def login(request):
	context = {'login_failed': False}
	if request.POST:
		email = request.POST['email']
		password = request.POST['password']
		user = auth.authenticate(request, email=email, password=password)
		if user:
			auth.login(request, user)
			return redirect("base_dashboard")
		else:
			context['login_failed'] = True
	return render(request, "public/login.html", context)

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			user = auth.authenticate(email=email, password=raw_password)
			auth.login(request, user)
			return redirect("base_dashboard")
	else:
		form = SignUpForm()
	return render(request, "public/signup.html", {'form': form})