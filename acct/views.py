from django.shortcuts import render
from .models import acct_attribute, User

# Create your views here.
def acc_attributes(request):
    
    users = acct_attribute.objects.all()
    context = {'users': users, 'authe':User}
    return render(request, 'acc_attributes.html', context)

def welcome(request):
    return render(request, 'welcome.html')