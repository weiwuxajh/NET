from django.db import models

# Create your models here.


class routes(models.Model):
    name = models.CharField(max_length=20)
    routetag = models.CharField(max_length=20)
    route = models.CharField(max_length=50)
    nexthop = models.CharField(max_length=20)