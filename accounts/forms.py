from django import forms
from .models import UserPro, User, Profile
from .widget import DatePickerInput
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import SetPasswordForm

class UserProForm(UserCreationForm):
    company = forms.CharField(label='Company', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Example Company Ltd'}))
    first_name = forms.CharField(label='First Name', max_length=20, min_length=5,
                             widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Name'}))
    date_of_birth = forms.DateField(label='Date of Birth', widget=DatePickerInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'you@example.com', 'id':'email'}), required=True)
    postcode = forms.CharField(label='Postcode', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'AD02534'}))
    location = forms.CharField(label='Location', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Accra'}))
    country =  CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={'class': 'form-me'}))
    number = PhoneNumberField(blank=True).formfield(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '+233557311180'}))
    
    # password1 = forms.CharField(label='Password', max_length=50, min_length=5,
    #                             widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # password2 = forms.CharField(label='Confirm Password',
    #                             max_length=50, min_length=5,
    #                              widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].required = True
        self.fields['first_name'].required = True
        self.fields['date_of_birth'].required = True
        self.fields['address'].required = True
        self.fields['email'].required = True
        self.fields['postcode'].required = True
        self.fields['location'].required = True
        self.fields['country'].required = True
        self.fields['number'].required = True


class UserWorkForm(UserCreationForm):
    company = forms.CharField(label='Company', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Example Company Ltd'}))
    first_name = forms.CharField(label='First Name', max_length=20, min_length=5,
                             widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Name'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'you@example.com', 'id':'email'}), required=True)
    number = PhoneNumberField(blank=True).formfield(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '+233557311180'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].required = True
        self.fields['first_name'].required = True
        self.fields['email'].required = True
        self.fields['number'].required = True

class ProfileForm(forms.ModelForm):

    class Meta: 
        model = Profile
        fields = ('image',)

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

