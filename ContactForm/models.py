from django.db import models

# Create your models here.


class ContactForm(models.Model):
    name = models.CharField(max_length=10000)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name, self.email
