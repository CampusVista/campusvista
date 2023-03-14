from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.acc_attributes, name='users'),
    # path('', views.welcome, name='welcome'),
    path('', views.dashboard, name='dashboard'),

]
