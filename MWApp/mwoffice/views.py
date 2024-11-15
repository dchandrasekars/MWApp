from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def mwoffice (request) :
   template = loader.get_template('myhome.html')
   return HttpResponse(template.render())

def login_user(request):
   pass

def logout_user(request):
   pass

