from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
    """
    View to render the login page or redirect authenticated users to the polls index.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered login.html template if the user is not authenticated.
        HttpResponseRedirect: Redirects to the polls index if the user is authenticated.
    """
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('polls:index'))
    else:
        return render(request, 'authentication/login.html')

def authenticate_user(request):
    """
    View to authenticate a user and log them in if credentials are valid.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the polls index if authentication is successful.
        HttpResponseRedirect: Redirects to the login page with an error message if authentication fails.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            messages.error(request, "Invalid username or password. Please try again or register.")
            return redirect('user_auth:login')
    else:
        return HttpResponseRedirect('user_auth:user_login')

def user_logout(request):
    """
    View to log out the current user.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the login page after logging out.
    """
    logout(request)
    return redirect('user_auth:login')

def show_user(request):
    """
    View to display the current user's username.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered user.html template with the current user's username.
    """
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

def register_user(request):
    """
    View to handle user registration.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered register.html template with the registration form.
        HttpResponseRedirect: Redirects to the login page after successful registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Registration Successful!")
                return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})
