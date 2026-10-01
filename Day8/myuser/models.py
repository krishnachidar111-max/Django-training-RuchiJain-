from django.db import models

class user(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.username
    

# Create your models here.
