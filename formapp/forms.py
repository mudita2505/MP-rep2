from django import forms
class Userregistration(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    password=forms.CharField(max_length=50)

