from django.contrib import admin
from django.urls import path
# from home import views
from . import views
admin.site.site_header = "Api Admin"
admin.site.site_title = "Api Admin Portal"
admin.site.index_title = "Welcome to Api Researcher Portal"

urlpatterns=[
        path("home",views.index,name='home'),
        path('',views.forms,name="forms"),
        # path(r'^(?P<countryname>[\w-]+)/$',views.query,name="query")
        path('query',views.query,name="query"),
        path('retrieve',views.retrieve,name="retrieve")
]