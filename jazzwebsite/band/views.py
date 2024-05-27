from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    """
    View function for the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home.html template.
    """
    return render(request, 'band/home.html')

def about(request):
    """
    View function for the about page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered about.html template.
    """
    return render(request, 'band/about.html')

def contact(request):
    """
    View function for the contact page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered contact.html template.
    """
    return render(request, 'band/contact.html')
