import uuid
import os


from django.db import models
import uuid


def getFileName(instance, filename):
    ext = filename.split('.')[-1]
    newFileName = f'{uuid.uuid4()}.{ext}'
    return os.path.join('product_photos/', newFileName)

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=150)
    bornDate = models.DateField()
    address = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to=getFileName,
        unique=True)

    def __str__(self):
        return self.name
