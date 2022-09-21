from django.contrib import admin
from django.urls import path
    # from home import views
from . import views
admin.site.site_header = "IceCream Admin"
admin.site.site_title = "IceCream Admin Portal"
admin.site.index_title = "Welcome to MyIceCream Researcher Portal"

urlpatterns=[
        path("home",views.index,name='home'),
        path('<a>,<b>',views.task2,name='task2'),
        path('',views.task3,name="task3"),
       
    ]