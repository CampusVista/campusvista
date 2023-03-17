import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, Http404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import acct_attribute, User, Student, ClassName, Staff

from django.http import JsonResponse


@login_required
def dashboard(request):
    # displays male and female students in template chart
    students = Student.objects.all()
    male_count = students.filter(rootid__gender='Male').count()
    female_count = students.filter(rootid__gender='Female').count()
    staff = Staff.objects.all()
    teachers_count = staff.filter(position="Teacher").count()
    staff_count = staff.filter(
        rootid__classification="Staff", position='Administrator').count()

    context = {
        'male_count': male_count,
        'female_count': female_count,
        'teachers': teachers_count,
        'staff': staff_count,
    }
    return render(request, 'account/dashboard.html', context)


@login_required
def acc_attributes(request):
    users = acct_attribute.objects.all()
    context = {'users': users, 'authe': User}
    return render(request, 'acc_attributes.html', context)
