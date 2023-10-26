from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    profession = models.CharField(max_length=100)
    entry_date = models.DateField()  # New field
    expiry_date = models.DateField()  # New field

    def __str__(self):
        return self.name
