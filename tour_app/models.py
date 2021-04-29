from django.db import models

# Create your models here.

class Tour(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    capacity = models.IntegerField()
    description = models.TextField()
    createdAt = models.DateTimeField(null=True, blank=True)
    updatedAt = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name