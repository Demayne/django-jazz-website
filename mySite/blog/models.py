from django.db import models

# Create your models here.
class Post(models.Model):
    """
    Model representing a blog post.

    Attributes:
        title (str): The title of the post.
        body (str): The content of the post.
        signature (str): The signature of the author, defaults to "Demayne Govender".
        date (datetime): The date and time the post was created.
    """
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Demayne Govender")
    date = models.DateTimeField()

    def __str__(self):
        """
        String representation of the Post model, returns the title of the post.
        """
        return self.title
