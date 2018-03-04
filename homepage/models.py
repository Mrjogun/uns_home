from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_year = models.PositiveSmallIntegerField(default=1)
    phone = models.CharField(max_length=11)
    account  = models.PositiveSmallIntegerField(default=0)