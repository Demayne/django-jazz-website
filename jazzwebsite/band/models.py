from django.db import models

# Create your models here.

class Band(models.Model):
    """
    Model representing a band.

    Attributes:
        name (str): The name of the band.
        description (str): A description of the band.
        image (ImageField): An image of the band.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        """
        String representation of the Band model, returns the band name.
        """
        return self.name
