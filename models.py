
from django.db import models

class formcontact(models.Model):
    #new.html
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    
