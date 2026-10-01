from django.db import models


class PortalUser(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class StudentRegistration(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    student_name = models.CharField(max_length=100)
    semester = models.CharField(max_length=30)
    subject = models.CharField(max_length=100)
    registered_by = models.ForeignKey(
        PortalUser,
        on_delete=models.CASCADE,
        related_name='student_registrations',
    )

    def __str__(self):
        return f'{self.student_id} - {self.student_name}'
