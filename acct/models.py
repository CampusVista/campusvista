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
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=50, default='')
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    #def __unicode__(self):
        #return 'acct_attribute {}'.format(self.id)
    
    def __str__(self):
        return '{} ({})'.format(self.rootid.username, self.classification)


class Student(models.Model):
    status = (
        ('Active', 'Active'),
        ('None Active', 'None Active'),
        ('Suspended', 'Suspended')
    )
    id = models.AutoField(primary_key=True, editable=False)
    rootid = models.ForeignKey(acct_attribute, on_delete=models.CASCADE)
    dob = models.DateField()
    status = models.CharField(max_length=20, choices=status, default='Active')
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    #def __unicode__(self):
       # return 'student {}'.format(self.id)
    def __str__(self):
        return f'{self.rootid} ({self.id})'
    
    
class Parent(models.Model):
    id = models.AutoField(primary_key=True)
    rootid = models.ForeignKey(acct_attribute, on_delete=models.CASCADE)
    students = models.ManyToManyField('Student')
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rootid)
    

class Subject(models.Model):
    subject_code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)
    
    def __str__(self):
        return f'{self.subject_code} ({self.name})'
        

class Staff(models.Model):
    position = (
        ('Headmaster', 'Headmaster'),
        ('Teacher', 'Teacher'),
        ('Administrator', 'Administrator'),
    )
    rootid = models.ForeignKey(acct_attribute, on_delete=models.CASCADE)
    position = models.CharField(max_length=20, choices=position)
    teach = models.ManyToManyField(Subject, through='Teaches')
    user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __str__(self):
        return f'{self.rootid} ({self.position})'
    
class Teaches(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.staff}'
    

class ClassName(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30)
    subject = models.ManyToManyField('Subject')
    class_teacher = models.ForeignKey(Staff, on_delete=models.CASCADE)
    #user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    class_id = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    date_from = models.DateField()
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __str__(self):
            return f'{self.student}'

class Fees(models.Model):
    status = (
        ('Fully Paid', 'Fully Paid'),
        ('Partially Paid', 'Partially Paid'),
        ('Not Paid', 'Not Paid')
    )
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    enrollment_id = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    class_id = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.CharField(max_length=20, choices=status, default='Active')
    paid_date = models.DateField()
    #user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __str__(self):
            return f'{self.student_id} ({self.paid_date})'

class Transcript(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_id = models.ForeignKey(ClassName, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark = models.CharField(max_length=10)
    grade = models.CharField(max_length=20)
    teacher_comments = models.CharField(max_length=100)
    #user = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    #def __unicode__(self):
       # return 'transcript {}'.format(self.id)
    def __str__(self):
        return self.student