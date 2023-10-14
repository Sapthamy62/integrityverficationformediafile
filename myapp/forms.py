from django import forms
from .models import Document

class upload(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
class VerifyForm(forms.Form):
    id=forms.IntegerField(label='Enter the id of the media file to be verified',required=True)     
class AdminForm(forms.Form):
    attrs={"type":"password"}
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter the email','class':'input_text'}), max_length=250)
    password=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the password','class':'input_text'}))   

class Register(forms.Form):
    attrs={"type":"password"}
    firstname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the firstname'}),max_length=250,required = True)  
    lastname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the lastname'}),max_length=250,required = True) 
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter the email'}), max_length=250,required = True)  
    password=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter the password'}),required = True)   
    
    