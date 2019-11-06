from django.db import models
from django import forms
 

class User(models.Model):
    '''用户表'''
    username = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    e_mail = models.CharField(max_length=128)

    def __str__(self):
        return self.username