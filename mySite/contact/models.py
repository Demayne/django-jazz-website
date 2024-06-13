from django.db import models

class ContactMessage(models.Model):
    """
    Model representing a contact message.

    Attributes:
        name (str): The name of the user.
        email (str): The email address of the user.
        phone_number (str): The phone number of the user.
        subject (str): The subject of the message.
        message (str): The content of the message.
        timestamp (datetime): The date and time the message was created.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representation of the ContactMessage model, returns the subject of the message.
        """
        return self.subject
