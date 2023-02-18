from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

# Create your models here.

class acct_attribute(models.Model):
    classification = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Staff', 'Staff'),
        ('Parent', 'Parent'),
    )
    gender = (
        ('Female', 'Female'),
        ('Male', 'Male')
    )
    rootid = models.ForeignKey(User, on_delete=models.CASCADE)
    classification = models.CharField(max_length=20, choices=classification)
    gender = models.CharField(max_length=10, choices=gender)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    user = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return 'acct_attribute {}'.format(self.id) 
