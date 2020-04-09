from django.db import models


class vlans(models.Model):
    name = models.CharField(max_length=20)
    vlanNum = models.CharField(max_length=20)
    vlanName = models.CharField(max_length=20)
    vlanInt = models.CharField(max_length=50)