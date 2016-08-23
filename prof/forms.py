from django import forms
from django.forms import ModelForm
from .models import Query, AgentQuery, NewAgentQuery, PatientProfile, PatientInfo, ContactUs, QueryImages #, Image
from django.db import models
from django.contrib.auth.models import User

class QueryForm(ModelForm):
    class Meta:
        model = Query
        fields = ['message']

class QueryImageForm(ModelForm):
    class Meta:
        model = QueryImages
        fields = ['photo']

class EmailPhoneForm(forms.Form):
    email = forms.EmailField(max_length=30)
    mobilenumber = forms.CharField(max_length=15)

class ProfileEditForm(forms.ModelForm):    
    class Meta:        
        model = User        
        fields = ['first_name','last_name','email']

class PatientProfileEditForm(forms.ModelForm):    
    class Meta:        
        model = PatientProfile        
        fields = ['date_of_birth','gender','allergies','medicalhistory','mobilenumber','photo']

class UserRegistrationForm(forms.ModelForm):    
    password = forms.CharField(label='Password',widget=forms.PasswordInput)    
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)
    
    class Meta:        
        model = User        
        fields = ['username','first_name','last_name','password']

    def clean_password2(self):        
        cd = self.cleaned_data        
        if cd['password'] != cd['password2']:            
            raise forms.ValidationError('Passwords don\'t match.')        
        return cd['password2'] 

class MailForm(forms.Form):
    to = forms.CharField(max_length=150)
    subject = forms.CharField(max_length=35)
    text_content = forms.CharField(max_length=150,initial='Text Content')
    html_content = forms.CharField(widget=forms.Textarea,initial='HTML Content')
    
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

class RESTAgentQueryForm(forms.ModelForm):
    class Meta:
        model = AgentQuery
        exclude = ['agent']


class AgentQueryForm(forms.ModelForm):
    class Meta:
        model = PatientInfo
        exclude = ['agent','query']
