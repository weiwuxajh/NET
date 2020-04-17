from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from Interface.query_devices import query_devices
from Interface.query_interfaces import query_interfaces
from Vlan.query_vlans import query_vlans
from Route.query_routes import query_routes
from Interface.config_interfaces import config_interfaces
from Vlan.config_vlans import config_vlans
from Route.config_routes import config_routes
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


class html_device(View):
    def get(self, request):
        return render(request, "query_device.html", {"test": "test"})


class config_int_ip(View):
    def get(self, request):
        return render(request, "config_int_ip.html", {"test": "test"})


class config_int_status(View):
    def get(self, request):
        return render(request, "config_int_status.html", {"test": "test"})


class config_vlan_creat(View):
    def get(self, request):
        return render(request, "config_vlan_creat.html", {"test": "test"})


class config_vlan_delete(View):
    def get(self, request):
        return render(request, "config_vlan_delete.html", {"test": "test"})


class config_vlan_access(View):
    def get(self, request):
        return render(request, "config_vlan_access.html", {"test": "test"})


class config_route_creat(View):
    def get(self, request):
        return render(request, "config_route_creat.html", {"test": "test"})


class config_route_delete(View):
    def get(self, request):
        return render(request, "config_route_delete.html", {"test": "test"})


class home(View):
    def get(self, request):
        return render(request, "home.html", {"test": "test"})


class check(View):
    def post(self, request):
        name = str(request.POST["username"])
        pwd = str(request.POST["passwd"])
        if name != None and not name.__eq__(""):
            if name == "admin" and pwd == "admin":
                return render(request, "home.html", {"test": "test"})
            else:
                return HttpResponse("0")
        else:
            return HttpResponse('0')


def login(request):
    return render(request, "login.html")


class device(View):
    def post(self,request):
        x = query_devices()
        y = x.query_device()
        # return HttpResponse(y)
        data = {}
        data['device'] = list(y)
        return JsonResponse(data)


class query_int_list(View):
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


class int_ip(View):
    def post(self,request):
        name = request.POST['name']
        port = request.POST['port']
        ip = request.POST['ip']
        x = config_interfaces(hostname=name,port=port,ip=ip)
        y = x.config_intip()
        # xx = json.dumps(y)
        # return JsonResponse(xx, safe=False)
        yy = {"bool":True}
        yyy = json.dumps(yy)
        return JsonResponse(yyy,safe=False)


class int_status(View):
    def post(self,request):
        name = request.POST['name']
        port = request.POST['port']
        status = request.POST['status']
        x = config_interfaces(hostname=name,port=port,status=status)
        y = x.config_int()
        # xx = json.dumps(y)
        # return JsonResponse(xx, safe=False)
        yy = {"bool":True}
        yyy = json.dumps(yy)
        return JsonResponse(yyy,safe=False)


class vlan_creat(View):
    def post(self,request):
        name = request.POST['name']
        vlanNum = request.POST['vlanNum']
        vlanName = request.POST['vlanName']
        x = config_vlans(hostname=name,vlanNum=vlanNum,vlanName=vlanName)
        y = x.creat_vlan()
        yy = {"bool": True}
        yyy = json.dumps(yy)
        return JsonResponse(yyy, safe=False)


class vlan_delete(View):
    def post(self,request):
        name = request.POST['name']
        vlanNum = request.POST['vlanNum']
        x = config_vlans(hostname=name,vlanNum=vlanNum)
        y = x.delete_vlan()
        yy = {"bool": True}
        yyy = json.dumps(yy)
        return JsonResponse(yyy, safe=False)


class vlan_access(View):
    def post(self,request):
        name = request.POST['name']
        vlanNum = request.POST['vlanNum']
        port = request.POST['port']
        x = config_vlans(hostname=name,vlanNum=vlanNum,port=port)
        y = x.configaccess()
        yy = {"bool": True}
        yyy = json.dumps(yy)
        return JsonResponse(yyy, safe=False)


class route_creat(View):
    def post(self,request):
        name = request.POST['name']
        port = request.POST['port']
        route = request.POST['route']
        netmask = request.POST['netmask']
        x = config_routes(hostname=name,net = route,nexthop=port,netmask=netmask)
        y = x.creat_route()
        yy = {"bool": True}
        yyy = json.dumps(yy)
        return JsonResponse(yyy, safe=False)


class route_delete(View):
    def post(self,request):
        name = request.POST['name']
        route = request.POST['route']
        netmask = request.POST['netmask']
        x = config_routes(hostname=name,net = route,netmask=netmask)
        y = x.delete_route()
        yy = {"bool": True}
        yyy = json.dumps(yy)
        return JsonResponse(yyy, safe=False)