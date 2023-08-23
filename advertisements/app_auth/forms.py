from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','first_name','last_name','password1','password2','email']
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower() 
        new = User.objects.filter(username = username) 
        if new.count(): 
            self.add_error('username',"Пользователь уже существует")
        return username 
    
    def clean_email(self): 
        email = self.cleaned_data['email'].lower() 
        new = User.objects.filter(email=email) 
        if new.count(): 
            self.add_error(email,"Адрес электронной почты уже существует")
        return email 

    def clean_password2(self): 
        password1 = self.cleaned_data['password1'] 
        password2 = self.cleaned_data['password2'] 

        if password1 and password2 and password1 != password2: 
            self.add_error(password2,"Пароли не совпадает")
        return password2 
