from django.db import models

# Create your models here.

class PotentialUser(models.Model):
    poten_user_email = models.EmailField(null=True, blank=True)