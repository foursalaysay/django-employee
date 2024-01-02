from django import forms

class UserForm(forms.Form):
    # Define your form fields here
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    contact = forms.CharField(max_length=20)
    address = forms.CharField(max_length=255)
