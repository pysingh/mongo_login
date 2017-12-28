from mongoengine import *
import datetime
from mongoengine import connect
connect('test_database', host='localhost', port=27017)

# Create your models here.
class User(Document):
    userName = StringField()
    userEmail = EmailField()
    userPassword = StringField()