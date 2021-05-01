
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include #for url
from my_app import views
from my_app.views import hours_add #for using offset from http://127.0.0.1:8000/time/plus/3/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="homepage"),
    path('new/',views.welcome,name="homepage"),
    #blank for homescreen
    #mapping the url to the index
    #default or optional
    path('date/',views.current),
    
    url(r'^time/plus/(\d{1,2})/$',views.hours_add),
    path('name/',views.name),
    path('add/',views.add),
    path('addd/',views.addd),
    path('stati/',views.stati),
    path('login/',views.sample),
    path('login/addr/',views.res),
    path('lab2/',views.det),
    path('lab2/details/',views.details),
    path('home/',views.ss,name="ss"),
    url(r'^time/plus/(\d+)/$',views.hours_add, name='hours_add'),
    #http://127.0.0.1:8000/time/plus/3/
    url(r'^days/plus/(\d+)/$',views.days_add, name='days_add'),
    #http://127.0.0.1:8000/days/plus/50/   
    path('age/',views.dob)    
]
