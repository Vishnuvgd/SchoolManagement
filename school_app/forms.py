
from django import forms

class AdminRegform(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    password=forms.CharField(max_length=25)
  

class AdminLogform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=25)

class Studentform(forms.Form):
    first_name = forms.CharField(max_length=50)  
    last_name = forms.CharField(max_length=50)  
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)
    
class OfficeForm(forms.Form):
    name = forms.CharField(max_length=25)  
    email = forms.EmailField() 
    password = forms.CharField(max_length=20)  
    desigination = forms.CharField(max_length=25)    
    subject = forms.CharField(max_length=25)    

class Libraryform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=10)