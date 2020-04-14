from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('int_list', views.html_int.as_view()),
    path('vlan_list', views.html_vlan.as_view()),
    path('route_list', views.html_route.as_view()),
    path('device_list', views.html_device.as_view()),
    path('configip', views.config_int_ip.as_view()),
    path('configstatus', views.config_int_status.as_view()),
    path('creatvlan', views.config_vlan_creat.as_view()),
    path('deletevlan', views.config_vlan_delete.as_view()),
    path('access', views.config_vlan_access.as_view()),
    path('creatroute', views.config_route_creat.as_view()),
    path('deleteroute', views.config_route_delete.as_view()),
    path('home', views.home.as_view()),
    path('device', views.device.as_view()),
    path('intlist',views.query_int_list.as_view()),
    path('vlanlist', views.query_vlan_list.as_view()),
    path('routelist', views.query_route_list.as_view()),
    path('int_ip', views.int_ip.as_view()),
    path('int_status', views.int_status.as_view()),
    path('vlan_creat', views.vlan_creat.as_view()),
    path('vlan_delete', views.vlan_delete.as_view()),
    path('vlan_access', views.vlan_access.as_view()),
    path('route_creat', views.route_creat.as_view()),
    path('route_delete', views.route_delete.as_view())
]