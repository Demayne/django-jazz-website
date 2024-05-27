from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_us(request):
    """
    View to handle the contact form submission.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered contact_us.html template with the contact form.
    """
    form_submitted = False
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form_submitted = True
            return render(request, 'contact_us.html', {'form_submitted': form_submitted})
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'form_submitted': form_submitted
    }
    return render(request, 'contact_us.html', context)

def contact_success(request):
    """
    View to display the success page after form submission.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered contact_success.html template.
    """
    return render(request, 'contact_success.html')
