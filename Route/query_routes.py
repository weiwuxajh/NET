#!/usr/bin/env python
# coding: utf-8
from netmiko import ConnectHandler
from Interface.models import devicelist
from Route.models import routes
import textfsm


class query_routes():
    def __init__(self,hostname='SW1'):
        self.hostname = hostname

    def query_route(self):
        list = devicelist.objects.all()
        fsm_results = []
        for index in range(len(list)):
            net_connect = ConnectHandler(device_type=list[index].devicetype,host=list[index].host,username=list[index].username,password=list[index].password)

            #执行命令，返回结果为字符串，赋值给output
            output = net_connect.send_command('show ip route')
            # print(output)
            net_connect.disconnect()
            TEMP_FILE = "./templates/query_routes_model"
            fsm = textfsm.TextFSM(open(TEMP_FILE))
            input_txt = output
            fsm_results.append(fsm.ParseText(input_txt))

        return fsm_results

    def query_db_route(self):
        route_list = routes.objects.values_list().filter(name = self.hostname)
        return route_list