from django.db import models

# Create your models here.

class Student(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    stdNumber = models.IntegerField()

    TEACHER = (
        ("ahmadi", "Ahmadi"),
        ("abdi", "Abdi"),
        ("nahrami", "Bahrami"),
    )

    teacher = models.CharField(max_length=200, choices=TEACHER)

    def __str__(self):
        return self.firstName + " " + self.lastName