from django.db import models

# Create your models here.
class Student(models.Model):
    S_Id = models.CharField(max_length=50, primary_key=True)
    S_Name = models.CharField(max_length=100)
    S_Pass = models.CharField(max_length=100)
    S_Email = models.EmailField(max_length=100)
    S_No = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.S_Name
