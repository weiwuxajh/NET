#!/usr/bin/env python
# coding: utf-8
from netmiko import ConnectHandler
from Interface.models import devicelist
import textfsm
from Route.models import routes


class config_routes():
    def __init__(self,hostname="SW1",net='2.2.2.0',netmask='255.255.255.0',nexthop='vlan1'):
        self.hostname = hostname
        self.net = net
        self.netmask = netmask
        self.nexthop = nexthop

    def creat_route(self):
        list = devicelist.objects.all()
        net_connect = ConnectHandler(device_type=list.get(name=self.hostname).devicetype,
                                     host=list.get(name=self.hostname).host,
                                     username=list.get(name=self.hostname).username,
                                     password=list.get(name=self.hostname).password,
                                     secret=list.get(name=self.hostname).secret)
        net_connect.enable()
        config_commands = ['ip route '+self.net+' '+self.netmask+" "+self.nexthop]
        net_connect.send_config_set(config_commands)
        output = net_connect.send_command('show ip route')
        net_connect.disconnect()
        i = routes(name = self.hostname,routetag='S',route=self.net,nexthop=self.nexthop)
        i.save()
        TEMP_FILE = "templates/query_routes_model"
        fsm = textfsm.TextFSM(open(TEMP_FILE))
        input_txt = output
        fsm_results = fsm.ParseText(input_txt)
        return fsm_results

    def delete_route(self):
        list = devicelist.objects.all()
        routelist = routes.objects.all()
        net_connect = ConnectHandler(device_type=list.get(name=self.hostname).devicetype,
                                     host=list.get(name=self.hostname).host,
                                     username=list.get(name=self.hostname).username,
                                     password=list.get(name=self.hostname).password,
                                     secret=list.get(name=self.hostname).secret)
        net_connect.enable()
        config_commands = ['no ip route ' + self.net + ' ' + self.netmask]
        net_connect.send_config_set(config_commands)
        output = net_connect.send_command('show ip route')
        net_connect.disconnect()
        routelist.filter(name=self.hostname, route=self.net).delete()
        TEMP_FILE = "templates/query_routes_model"
        fsm = textfsm.TextFSM(open(TEMP_FILE))
        input_txt = output
        fsm_results = fsm.ParseText(input_txt)
        return fsm_results
