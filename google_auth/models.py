from django.db import models

class GUser(models.Model):
    email = models.EmailField()

class Credentials(models.Model):
    credentials = models.CharField(max_length=3000)
    email = models.EmailField()
    user = models.ForeignKey(GUser)
