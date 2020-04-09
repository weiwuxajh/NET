#!/usr/bin/env python
# coding: utf-8

from Interface.models import devicelist
from django.http import HttpResponse,JsonResponse
import json


class query_devices():
    def __init__(self,name='SW3',devicetype='cisco_ios',host='1.1.1.1',username='j',password='cisco',secret='cisco'):
        self.name = name
        self.devicetype = devicetype
        self.host = host
        self.username = username
        self.password = password
        self.secret = secret

    def query_device(self):
        device = devicelist.objects.values_list()
        return device

    def add_device(self):
        i = devicelist(name=self.name,devicetype=self.devicetype,host=self.host,username=self.username,password=self.password,secret=self.secret)
        i.save()
        return 'OK'

    def delete_device(self):
        i = devicelist.objects.all()
        i.filter(name = self.name).delete()
        return 'delete'