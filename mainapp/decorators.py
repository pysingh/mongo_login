from django.shortcuts import render, redirect

def login_required(function):
    def wrap(request, *args, **kwargs):
        if 'authenticate' in request.session:
        	if request.session['authenticate']:
        		return function(request, *args, **kwargs)
        return redirect('login')
    return wrap