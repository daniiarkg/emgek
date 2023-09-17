from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Report(models.Model):
    date_in = models.DateField(null=True)
    speciality = models.CharField(max_length=100, null=True)
    date_out = models.DateField(null=True)
    reason_out = models.CharField(max_length=100, null=True)


class Org(models.Model):
    name = models.CharField(
        verbose_name='Наименование организации', max_length=200, null=True)


class E_user(AbstractUser):
    current_org = models.ForeignKey(Org, on_delete=models.CASCADE)
