from django.contrib import admin
from account.models import acct_classification, acct_attribute

admin.site.register(acct_classification)
admin.site.register(acct_attribute)