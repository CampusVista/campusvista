from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 


def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

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
    gender = models.CharField(max_length=20, choices=gender)
    phone = models.IntegerField()
    address = models.CharField(max_length=50, default='')
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return 'acct_attribute {}'.format(self.id)


class student(models.Model):
    status = (
        ('Active', 'Active'),
        ('None Active', 'None Active'),
        ('Suspended', 'Suspended')
    )
    rootid = models.ForeignKey(acct_attribute, on_delete=models.CASCADE)
    dob = models.DateField()
    parent_id = models.IntegerField()
    status = models.CharField(max_length=20, choices=status, default='Active')
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return 'student {}'.format(self.id)

class staff(models.Model):
    position = (
        ('Headmaster', 'Headmaster'),
        ('Teacher', 'Teacher'),
        ('Administrator', 'Administrator'),
    )
    rootid = models.ForeignKey(acct_attribute, on_delete=models.CASCADE)
    position = models.CharField(max_length=20, choices=position)
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return 'staff {}'.format(self.id)

class subjectName(models.Model):
    subject = (
        ('English', 'English'),
        ('Mathmatics', 'Mathmatics'),
        ('History', 'History'),
        ('Shona', 'Shona'),
    )
    rootid = models.ForeignKey(acct_attribute, on_delete=models.CASCADE)
    name = models.CharField(max_length=30,choices=subject, default='')
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return 'subjectName {}'.format(self.id)

class className(models.Model):
    className = (
        ('Form 1 - Blue', 'Form 1 - Blue'),
        ('Form 1 - Red', 'Form 1 - Red'),
        ('Form 1 - Green', 'Form 1 - Green'),
        ('Form 2 - Blue', 'Form 2 - Blue'),
        ('Form 2 - Red', 'Form 2 - Red'),
        ('Form 2 - Green', 'Form 2 - Green'),
    )
    name = models.CharField(max_length=30,choices=className, default='')
    teacher_id = models.IntegerField()
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return 'className {}'.format(self.id)


class enrollment(models.Model):
    rootid = models.ForeignKey(student, on_delete=models.CASCADE)
    staff_id = models.IntegerField()
    class_id = models.ForeignKey(className, on_delete=models.CASCADE)
    date_from = models.DateField()
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return 'enrollment {}'.format(self.id)

class fees(models.Model):
    status = (
        ('Fully Paid', 'Fully Paid'),
        ('Partially Paid', 'Partially Paid'),
        ('Not Paid', 'Not Paid')
    )
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    enrollment_id = models.ForeignKey(enrollment, on_delete=models.CASCADE)
    class_id = models.ForeignKey(className, on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.CharField(max_length=20, choices=status, default='Active')
    paid_date = models.DateField()
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return 'fees {}'.format(self.id)

class transcript(models.Model):
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    class_id = models.ForeignKey(className, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subjectName, on_delete=models.CASCADE)
    mark = models.CharField(max_length=10)
    grade = models.CharField(max_length=20)
    teacher_comments = models.CharField(max_length=100)
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return 'transcript {}'.format(self.id)