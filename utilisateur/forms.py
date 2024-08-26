from django import forms


from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class SugnUpForm(UserCreationForm):
    
    email = forms.EmailField(max_length=250,help_text='Requis. Entrer une adresse email  valide.')
    
    class Meta:
       model = User
       
       fields =('username','password1','password2',)
       