from django.shortcuts import render

def about_view(request):
    """
    View to render the 'about' page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered about.html template.
    """
    return render(request, 'about.html')

def childhood1_view(request):
    """
    View to render the 'childhood1' page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered childhood1.html template.
    """
    return render(request, 'childhood1.html')

def javaScript_view(request):
    """
    View to render the 'javaScript' page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered javaScript.html template.
    """
    return render(request, 'javaScript.html')
