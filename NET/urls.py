"""NET URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import testdb
from Interface.config_interfaces import config_interfaces
from Interface import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('testdb',testdb.testdb),
    path('testvlan',testdb.testvlan),
    path('testroute',testdb.testroute),
    path('configint',views.int.as_view()),
    path('configvlan', views.vlan.as_view()),
    path('configroute', views.route.as_view()),
    path('device', views.device.as_view()),
    path('intlist',views.query_int_list.as_view()),
    path('routelist', views.query_route_list.as_view()),
    path('vlanlist', views.query_vlan_list.as_view())
]
