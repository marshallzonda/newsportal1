from django.db import models

class User(models.Model):
    login = models.CharField(max_length=40)
    passw = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    regdate = models.DateTimeField()
    status = models.CharField(max_length=40)
