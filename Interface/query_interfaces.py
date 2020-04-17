#!/usr/bin/env python
# coding: utf-8
from netmiko import ConnectHandler
from Interface.models import interfaces
from Interface.models import devicelist
import textfsm


class query_interfaces():
    def __init__(self,hostname='SW1'):
        self.hostname = hostname

    def query_int(self):
        list = devicelist.objects.all()
        fsm_results = []
        for index in range(len(list)):
            net_connect = ConnectHandler(device_type=list[index].devicetype,host=list[index].host,username=list[index].username,password=list[index].password)
            #找到目前所在视图
            # current_view = net_connect.find_prompt()
            # print(current_view)
            output = net_connect.send_command('show ip int brief')
            net_connect.disconnect()
            TEMP_FILE = "templates/query_interfaces_model"
            fsm = textfsm.TextFSM(open(TEMP_FILE))
            input_txt = output
            fsm_results.append(fsm.ParseText(input_txt))
        return fsm_results

    def query_db_int(self):
        int_list = interfaces.objects.values_list().filter(name = self.hostname)
        return int_list



