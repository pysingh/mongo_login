import datetime
from django.shortcuts import render, HttpResponse, redirect
from bson.json_util import loads
from mainapp.decorators import login_required
from mainapp.models import User


def populateUser():
	obj = User()
	obj.usernName = 'piyushps09'
	obj.userEmail = 'abc@gmail.com'
	obj.userPassword = '12345'
	obj.save()

# Create your views here.
def login(request):
	# userData = {"name": "Piyush","email": "abc@gmail.com","password": "12345"}
	# populateUser(userData)
	if 'authenticate' in request.session:
		if request.session['authenticate'] == True:
			return redirect('home')
	return render(request, 'login.html', context={})

def logout(request):
	if 'authenticate' in request.session:
		request.session['authenticate'] = False
	return redirect('login')

def auth(request):
	if request.method == 'POST':
		email = request.POST.get('email', '')
		password = request.POST.get('pwd', '')
		if email != '' and password != '':
			user = User.objects(userEmail=email, userPassword=password)
			if user:
				request.session['authenticate'] = True
				return redirect('home')
		return render(request, 'login.html', context={'message': 'Wrong username or password!'})
	else:
		return redirect('login')
@login_required
def home(request):
	return render(request, 'home.html', context={})
