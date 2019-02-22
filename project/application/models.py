from __future__ import unicode_literals
from django.db import models


class Reg(models.Model):
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100,default='Btech')
    college=models.CharField(max_length=500,default='BCET Gurdaspur')
    email=models.EmailField(max_length=100,unique=True)
    contact_no=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)

class Event(models.Model):
    participant=models.CharField(max_length=100)
    event=models.CharField(max_length=30)
class Querry(models.Model):
    mobile_no=models.CharField(max_length=20)
    query=models.CharField(max_length=500)