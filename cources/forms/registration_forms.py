from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control '}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    email = forms.EmailField(max_length=50, required=True, widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email =  self.cleaned_data['email']
        user = None
        try:
            user = User.objects.get(email = email)
        except:
            return email
        
        if user is not None:
            return ValidationError('User alreqady Exists ..!!')