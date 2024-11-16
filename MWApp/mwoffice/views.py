from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def home(request):
   if request.method=='POST':
      uname=request.POST['uname']
      upass=request.POST['upass']

      #authenicate
      user=authenticate(request,username=uname,password=upass)
      if user is not None:
         login(request,user)
         #messages.success(request,"you logged")
         return redirect('home')
      else:
         messages.success(request,"Invalid Credentials..try again")
         return redirect('home')
   else:
      return render(request,'home.html',{})

def login_user(request):
   pass

def logout_user(request):
   logout(request)
   messages.success(request,"Logged Out..")
   return redirect('home')


def register_user(request):   
      return render(request,'register.html')

