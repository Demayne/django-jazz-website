from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    """
    Form for users to submit contact messages.
    
    Fields:
        - name: The name of the user.
        - email: The email address of the user.
        - phone_number: The phone number of the user.
        - subject: The subject of the message.
        - message: The content of the message.
    """
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone_number', 'subject', 'message']
