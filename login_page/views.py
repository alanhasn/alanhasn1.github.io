# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# Define a view function for the login page
def Login(request):
    # Check if the HTTP request method is POST 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
         
        # Authenticate the user with the provided username and password
        user = authenticate(username=username, password=password)
         
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            # return redirect('/main/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('main')
     
    # Render the login page template (GET request)
    return render(request, 'html/login.html')


def Forgot_Password(request):
    return render(request, 'html/forgot_password.html')