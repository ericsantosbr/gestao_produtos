import uuid
import os
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from decouple import config
from django.db import models


def GetImageUuid4Name(instance, filename: str):
    return (config('MEDIA_PRODUCT_IMAGES_FOLDER', default='product_photos/')) + GetUuid4Name(filename=filename)

def GetUuid4Name(filename: str):
    ext = filename.split('.')[-1]
    new_file_name = f'{uuid.uuid4()}.{ext}'
    return new_file_name


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
        upload_to=GetImageUuid4Name,
        unique=True)
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000000)])
    description = models.CharField(max_length=20000)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'id#:{self.id}; post_id:{self.post_id}; content:{self.content[0:50]}'