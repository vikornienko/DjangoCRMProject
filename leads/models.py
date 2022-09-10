from django.db import models

class Lead(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField(default=0)

