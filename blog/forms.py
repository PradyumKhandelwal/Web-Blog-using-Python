from dataclasses import field, fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

from blog.models import Post

# class PostForm(forms.ModelForm):
#     pass


class PostForm(forms.ModelForm):
     

    class Meta:
        model = Post
        fields = ["author","title","text"] #"__all__"
        # fields of the model
    # first_name = forms.CharField(max_length = 200)
    # last_name = forms.CharField(max_length = 200)
    # roll_number = forms.IntegerField(
    #                  help_text = "Enter 6 digit roll number"
    #                  )
    # password = forms.CharField(widget = forms.PasswordInput())
    #  Author = forms.Select(choices=INTEGER_CHOICES)
    #  Title = forms.CharField(max_length=100)
    #  Text = forms.CharField


