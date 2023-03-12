import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, Http404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import acct_attribute, User


@login_required
def welcome(request):
    return render(request, 'welcome.html')

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')

@login_required
def acc_attributes(request):
    
    users = acct_attribute.objects.all()
    context = {'users': users, 'authe':User}
    return render(request, 'acc_attributes.html', context)

