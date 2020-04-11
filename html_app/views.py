from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from Interface.query_devices import query_devices
from Interface.query_interfaces import query_interfaces
from Vlan.query_vlans import query_vlans
from Route.query_routes import query_routes
import json

# Create your views here.


class html_int(View):
    def get(self, request):
        return render(request, "query_interface.html", {"test": "test"})


class html_vlan(View):
    def get(self, request):
        return render(request, "query_vlan.html", {"test": "test"})


class html_route(View):
    def get(self, request):
        return render(request, "query_route.html", {"test": "test"})



class device(View):
    def post(self,request):
        x = query_devices()
        y = x.query_device()
        # return HttpResponse(y)
        data = {}
        data['device'] = list(y)
        return JsonResponse(data)


class query_int_list(View):
    # def get(self,request):
    #     x = query_interfaces()
    #     y = x.query_db_int()
    #     data = {}
    #     data['int'] = list(y)
    #     # return HttpResponse(data)
    #     return JsonResponse(data)

    def post(self,request):
        name = request.POST['name']
        x = query_interfaces(hostname=name)
        y = x.query_db_int()
        data = {}
        data['int'] = list(y)
        return JsonResponse(data)


class query_vlan_list(View):
    def post(self,request):
        name = request.POST['name']
        x = query_vlans(hostname=name)
        y = x.query_db_vlan()
        data = {}
        data['vlan'] = list(y)
        return JsonResponse(data)


class query_route_list(View):
    def post(self,request):
        name = request.POST['name']
        x = query_routes(hostname=name)
        y =x.query_db_route()
        data = {}
        data['route'] = list(y)
        return JsonResponse(data)

