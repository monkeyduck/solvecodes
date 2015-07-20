'''
Created on 2014-3-16

@author: lilinchuan
'''
from django import forms
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirm',widget=forms.PasswordInput)
    def pwd_validate(self,p1,p2):
        return p1==p2
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class ChangepwdForm(forms.Form):
    old_pwd = forms.CharField(label='Old password',widget=forms.PasswordInput)
    new_pwd = forms.CharField(label='New password',widget=forms.PasswordInput)
    new_pwd2= forms.CharField(label='Confirm password',widget=forms.PasswordInput)    