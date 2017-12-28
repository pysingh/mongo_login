import datetime
from django.shortcuts import render, HttpResponse
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.test_database
users = db.test_users

from random import randint

def populateUser(data):
	id_ = users.insert_one(data)
# Create your views here.
def login(request):
	# userData = {"name": "Piyush","email": "abc@gmail.com","password": "12345"}
	data = users.find_one({'email': "abc@gmail.com"})
	print(data)
	return render(request, 'login.html', context={})

def home(request):
	import pdb;pdb.set_trace()
	return render(request, 'home.html', context={})