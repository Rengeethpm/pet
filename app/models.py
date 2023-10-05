from django.contrib.auth.models import AbstractUser
from django.db import models




class Register(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    contact_no = models.CharField(max_length=10)
    address = models.CharField(max_length=150)


    def __str__(self):
        return self.username


class Pet(models.Model):
    breed = models.CharField(max_length=25)
    age = models.IntegerField(null=False)
    medical_certificate = models.FileField()


    def __str__(self):
        return self.breed




