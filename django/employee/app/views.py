from django import forms
from django.shortcuts import render
from django.http import HttpResponse

class UserForm(forms.Form):
    # Define your form fields here
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    contact = forms.CharField(max_length=20)
    address = forms.CharField(max_length=255)

def signup_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Process valid form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            address = form.cleaned_data['address']

            # Perform actions based on form data
            # Add your logic here

            return HttpResponse("Form submitted successfully!")
    else:
        form = UserForm()

    return render(request, 'frontpage.html', {'form': form})
