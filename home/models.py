import uuid
import os
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

from django.db import models
import uuid


def GetFileName(instance, filename):
    ext = filename.split('.')[-1]
    new_file_name = f'{uuid.uuid4()}.{ext}'
    return os.path.join('product_photos/', new_file_name)


class States(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Regions(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(States, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubRegions(models.Model):
    name = models.CharField(max_length=120)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to=GetFileName,
        unique=True)
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000000)])
    description = models.CharField(max_length=20000)

    def __str__(self):
        return self.name
