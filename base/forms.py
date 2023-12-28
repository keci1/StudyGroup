from django import forms
from .models import Room
from django.contrib.auth.models import User
from .models import CustomUser 

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser  
        fields = ['name', 'email', 'bio', 'avatar']