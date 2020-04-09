
# !/usr/bin/env python

# -*- coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals

from celery import shared_task

from Interface.models import interfaces
from Interface.query_interfaces import query_interfaces
from Interface.models import devicelist
from Vlan.query_vlans import query_vlans
from Vlan.models import vlans
from Route.models import routes
from Route.query_routes import query_routes



@shared_task
def add():
    x = query_interfaces()
    y = x.query_int()
    # print(y)
    list = devicelist.objects.all()
    interfaces.objects.all().delete()
    for index in range(len(y)):
        for x in range(5):
            i = interfaces(name=list.get(id=index + 1).name, interface=y[index][x][0], ipadd=y[index][x][1],status=y[index][x][2])
            i.save()
    return "ip"


@shared_task
def addvlan():
    x = query_vlans()
    y = x.query_vlan()
    list = devicelist.objects.all()
    vlans.objects.all().delete()
    for index in range(len(y)):
        for x in range(len(y[index])):
            i = vlans(name=list.get(id=index + 1).name, vlanNum=y[index][x][0], vlanName=y[index][x][1],
                      vlanInt=y[index][x][2])
            i.save()
    return "vlan"


@shared_task
def addroute():
    x = query_routes()
    y = x.query_route()
    list = devicelist.objects.all()
    routes.objects.all().delete()
    for index in range(len(y)):
        for x in range(len(y[index])):
            i = routes(name=list.get(id=index + 1).name, routetag=y[index][x][0], route=y[index][x][1],
                       nexthop=y[index][x][2])
            i.save()
    return "route"