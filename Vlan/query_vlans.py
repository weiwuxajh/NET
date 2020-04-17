#!/usr/bin/env python
# coding: utf-8
from netmiko import ConnectHandler
from Interface.models import devicelist
from Vlan.models import vlans
import textfsm


class query_vlans():
    def __init__(self, hostname='SW1'):
        self.hostname = hostname

    def query_vlan(self):
        list = devicelist.objects.all()
        fsm_results = []
        for index in range(len(list)):
            net_connect = ConnectHandler(device_type=list[index].devicetype,host=list[index].host,username=list[index].username,password=list[index].password)
            output = net_connect.send_command('show vlan b')
            net_connect.disconnect()

            TEMP_FILE = "./templates/query_vlans_model"
            fsm = textfsm.TextFSM(open(TEMP_FILE))
            input_txt = output
            fsm_results.append(fsm.ParseText(input_txt))
        return fsm_results

    def query_db_vlan(self):
        vlan_list = vlans.objects.values_list().filter(name = self.hostname)
        return vlan_list