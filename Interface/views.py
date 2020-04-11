from django.shortcuts import render
from Interface.config_interfaces import config_interfaces
from Interface.query_interfaces import query_interfaces
from Route.query_routes import query_routes
from Vlan.query_vlans import query_vlans
from django.http import HttpResponse,JsonResponse
from django.views import View
from Vlan.config_vlans import config_vlans
import json
from Route.config_routes import config_routes
from Interface.query_devices import query_devices
from django.shortcuts import render
from django.core import serializers
# Create your views here.


class int(View):
    def get(self,request):
        x = config_interfaces()
        y = x.config_intip()
        xx = json.dumps(y)
        return JsonResponse(xx, safe=False)#config


class vlan(View):
    def get(self,request):
        x = config_vlans()
        y = x.delete_vlan()
        xx = json.dumps(y)
        return JsonResponse(xx, safe=False)


class route(View):
    def get(self,request):
        x = config_routes()
        y = x.delete_route()
        xx = json.dumps(y)
        return JsonResponse(xx, safe=False)


# class device(View):
#     def get(self,request):
#         x = query_devices()
#         y = x.query_device()
#         # return HttpResponse(y)
#         data = {}
#         data['device'] = list(y)
#         return JsonResponse(data)


# class query_int_list(View):
#     def get(self,request):
#         x = query_interfaces()
#         y = x.query_db_int()
#         data = {}
#         data['int'] = list(y)
#         return JsonResponse(data)


# class query_route_list(View):
#     def get(self,request):
#         x = query_routes()
#         y =x.query_db_route()
#         data = {}
#         data['route'] = list(y)
#         return JsonResponse(data)


# class query_vlan_list(View):
#     def get(self,request):
#         x = query_vlans()
#         y = x.query_db_vlan()
#         data = {}
#         data['vlan'] = list(y)
#         return JsonResponse(data)

