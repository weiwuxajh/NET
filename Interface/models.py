from django.db import models


class interfaces(models.Model):
    name = models.CharField(max_length=20)
    interface = models.CharField(max_length=20)
    ipadd = models.CharField(max_length=20)
    status = models.CharField(max_length=20)


class devicelist(models.Model):
    name = models.CharField(max_length=20)
    devicetype = models.CharField(max_length=20)
    host = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    secret = models.CharField(max_length=20)