from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




class Organisation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Employee(AbstractUser):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, unique=True)
    def __str__(self):
        return self.username


class Task(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title