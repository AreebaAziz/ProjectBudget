from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def index(request):
	return redirect('login')

@login_required(login_url='/login')
def base_dashboard(request):
	return render(request, "dashboard.html", context={'user': request.user})