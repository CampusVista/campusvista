from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

# Create your models here.

class acct_clasification(models.Model):
    rootid = models.IntegerField()
    classification = models.CharField(max_length=20, default='student')
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return 'acct_clasification {}'.format(self.id) 
