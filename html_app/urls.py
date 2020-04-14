from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('int_list', views.html_int.as_view()),
    path('vlan_list', views.html_vlan.as_view()),
    path('route_list', views.html_route.as_view()),
    path('device_list', views.html_device.as_view()),
    path('configip', views.config_int.as_view()),
    path('home', views.home.as_view()),
    path('device', views.device.as_view()),
    path('intlist',views.query_int_list.as_view()),
    path('vlanlist', views.query_vlan_list.as_view()),
    path('routelist', views.query_route_list.as_view()),
    path('int', views.int.as_view())
]