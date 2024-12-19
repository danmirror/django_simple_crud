from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64)
    old = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return (f"ID:{self.id}, name:{self.name}, old:{self.old}, number:{self.number}")

