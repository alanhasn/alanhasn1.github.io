# accounts/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import re  # Regular expression module for password validation

def is_strong_password(password):

    if (len(password) < 8 or
            not re.search(r"[A-Z]", password) or  # At least one uppercase letter
            not re.search(r"[a-z]", password) or  # At least one lowercase letter
            not re.search(r"[0-9]", password) or  # At least one digit
            not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):  # At least one special character
        return False  # Password does not meet criteria
    return True  # Password is strong

def SignUp(request):

    if request.method == "POST":
        username = request.POST.get("username")  # Get username from form
        email = request.POST.get("email")  # Get email from form
        password = request.POST.get("password")  # Get password from form

        # Check if username already exists in the database
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return render(request, 'html/signup.html')  # Render the signup form with an error message

        # Check if email already exists in the database
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered. Please use a different one.")
            return render(request, 'html/signup.html')  # Render the signup form with an error message

        # Validate password strength
        if not is_strong_password(password):
            messages.error(request, 'Password must be at least 8 characters long, and include uppercase letters, lowercase letters, numbers, and special characters.')
            return render(request, 'html/signup.html')  # Render the signup form with an error message

        try:
            # Create and save the new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()  # Save the user to the database
            messages.success(request, 'Signup successful! You can now log in.')
            return redirect("login")  # Redirect to the login page

        except ValidationError as v:
            messages.error(request, f'Error creating user: {v}')  # Handle validation errors
            return render(request, 'html/signup.html')  # Render the signup form with an error message
        except Exception as e:
            messages.error(request, f'An unexpected error occurred: {e}')  # Handle unexpected errors
            return render(request, 'html/signup.html')  # Render the signup form with an error message

    else:
        return render(request, 'html/signup.html')  # Render the signup form for GET requests

def logout(request):
    """
    Handle user logout.
    Clear the user session and redirect to the main page.
    """
    request.session.flush()  # Clear the user session
    return redirect(reverse('main'))  # Redirect to the home page, replace 'main' with your URL name