#!/usr/bin/env python
# coding: utf-8
from netmiko import ConnectHandler
from Interface.models import devicelist
import textfsm
from Vlan.models import vlans


class config_vlans():
    def __init__(self,hostname='SW1',vlanNum='34',vlanName='t1',port='Ethernet0/3'):
        self.hostname = hostname
        self.vlanNum = vlanNum
        self.vlanName = vlanName
        self.port = port

    def creat_vlan(self):
        list = devicelist.objects.all()
        net_connect = ConnectHandler(device_type=list.get(name=self.hostname).devicetype,
                                     host=list.get(name=self.hostname).host,
                                     username=list.get(name=self.hostname).username,
                                     password=list.get(name=self.hostname).password,
                                     secret=list.get(name=self.hostname).secret)
        net_connect.enable()
        config_commands = ['vlan '+self.vlanNum, 'name '+self.vlanName]
        net_connect.send_config_set(config_commands)
        output = net_connect.send_command('show vlan b')
        net_connect.disconnect()
        i = vlans(name = self.hostname,vlanNum=self.vlanNum,vlanName=self.vlanName,vlanInt='')
        i.save()
        TEMP_FILE = "templates/query_vlans_model"
        fsm = textfsm.TextFSM(open(TEMP_FILE))
        input_txt = output
        fsm_results = fsm.ParseText(input_txt)
        return fsm_results

    def delete_vlan(self):
        list = devicelist.objects.all()
        vlanlist = vlans.objects.all()
        net_connect = ConnectHandler(device_type=list.get(name=self.hostname).devicetype,
                                     host=list.get(name=self.hostname).host,
                                     username=list.get(name=self.hostname).username,
                                     password=list.get(name=self.hostname).password,
                                     secret=list.get(name=self.hostname).secret)
        net_connect.enable()
        config_commands = ["no vlan "+self.vlanNum]
        net_connect.send_config_set(config_commands)
        output = net_connect.send_command('show vlan b')
        net_connect.disconnect()
        vlanlist.filter(name=self.hostname,vlanNum=self.vlanNum).delete()
        TEMP_FILE = "templates/query_vlans_model"
        fsm = textfsm.TextFSM(open(TEMP_FILE))
        input_txt = output
        fsm_results = fsm.ParseText(input_txt)
        return fsm_results

    def configaccess(self):
        list = devicelist.objects.all()
        vlanlist = vlans.objects.all()
        net_connect = ConnectHandler(device_type=list.get(name=self.hostname).devicetype,
                                     host=list.get(name=self.hostname).host,
                                     username=list.get(name=self.hostname).username,
                                     password=list.get(name=self.hostname).password,
                                     secret=list.get(name=self.hostname).secret)
        net_connect.enable()
        config_commands = ["interface "+self.port,'switchport mode access','switchport access vlan '+self.vlanNum]
        net_connect.send_config_set(config_commands)
        output = net_connect.send_command('show vlan b')
        net_connect.disconnect()
        # vlanlist.filter(name=self.hostname,vlanNum=self.vlanNum).
        TEMP_FILE = "templates/query_vlans_model"
        fsm = textfsm.TextFSM(open(TEMP_FILE))
        input_txt = output
        fsm_results = fsm.ParseText(input_txt)
        return fsm_results
