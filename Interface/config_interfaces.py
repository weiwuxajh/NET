#!/usr/bin/env python
# coding: utf-8
from netmiko import ConnectHandler
from Interface.models import devicelist
import textfsm
from Interface.models import interfaces
from django.http import HttpResponse


class config_interfaces():
    def __init__(self,hostname='SW1',port="vlan40",status="no shutdown",ip="3.3.3.3",netmask="255.255.255.0"):
        self.hostname = hostname
        self.port = port
        self.status = status
        self.ip = ip
        self.netmask = netmask

    def config_int(self):
        list =devicelist.objects.all()
        intlist = interfaces.objects.all()
        net_connect = ConnectHandler(device_type=list.get(name=self.hostname).devicetype, host=list.get(name=self.hostname).host,username=list.get(name=self.hostname).username, password=list.get(name=self.hostname).password,secret=list.get(name=self.hostname).secret)
        net_connect.enable()
        config_commands = ['interface ' + self.port, self.status]
        net_connect.send_config_set(config_commands)
        output = net_connect.send_command('show ip int b')
        net_connect.disconnect()
        intlist.filter(name=self.hostname,interface=self.port).update(status=self.status)
        interfaces.objects.get(name=self.hostname,interface=self.port).save()
        TEMP_FILE = "templates/query_interfaces_model"
        fsm = textfsm.TextFSM(open(TEMP_FILE))
        input_txt = output
        fsm_results = fsm.ParseText(input_txt)
        return fsm_results

    def config_intip(self):
        list = devicelist.objects.all()
        intlist = interfaces.objects.all()
        net_connect = ConnectHandler(device_type=list.get(name=self.hostname).devicetype,
                                     host=list.get(name=self.hostname).host,
                                     username=list.get(name=self.hostname).username,
                                     password=list.get(name=self.hostname).password, secret=list.get(name=self.hostname).secret)
        net_connect.enable()
        config_commands = ['interface ' + self.port,self.status,'ip address '+self.ip+' '+self.netmask]
        net_connect.send_config_set(config_commands)
        output = net_connect.send_command('show ip int b')
        net_connect.disconnect()
        # i = interfaces(name=self.hostname,interface=self.port,ipadd=self.ip,status='up')
        # i.save()
        intlist.filter(name=self.hostname).delete()
        TEMP_FILE = "templates/query_interfaces_model"
        fsm = textfsm.TextFSM(open(TEMP_FILE))
        input_txt = output
        fsm_results = fsm.ParseText(input_txt)
        for index in range(len(fsm_results)):
            i = interfaces(name=self.hostname, interface=fsm_results[index][0], ipadd=fsm_results[index][1],
                           status=fsm_results[index][2])
            i.save()
        return fsm_results

