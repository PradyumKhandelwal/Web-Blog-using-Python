from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
# class PostForm(forms.ModelForm):
#     pass


class GeeksModel(forms.Form):
        # fields of the model
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    roll_number = forms.IntegerField(
                     help_text = "Enter 6 digit roll number"
                     )
    password = forms.CharField(widget = forms.PasswordInput())
   
    # def __str__(self):
    #     return self.description
# class UserRegisterForm(UserCreationForm):
# 	email = forms.EmailField()
# 	phone_no = forms.CharField(max_length = 20)
# 	first_name = forms.CharField(max_length = 20)
# 	last_name = forms.CharField(max_length = 20)
# 	class Meta:
# 		model = User
# 		fields = ['username', 'email', 'phone_no', 'password1', 'password2']

# print("Hello World")
