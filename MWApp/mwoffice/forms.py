from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    empno=forms.IntegerField()
    ename=forms.CharField()
    phone=forms.IntegerField()
    

class Meta:
    model=User
    fields=('username','ename','empno','phoneno','password1','password2')

def __str__(self):
    return f"{self.username} {self.password1} {self.password2}"