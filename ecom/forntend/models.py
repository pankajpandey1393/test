from distutils.command.upload import upload
from django.db import models

class product(models.Model):
    productname =models.CharField(max_length=280)
    price=models.IntegerField(max_length=5)
    description=models.TextField()
    image=models.FileField(upload_to='products')

