from email import message
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.first_name

    class Meta:
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'