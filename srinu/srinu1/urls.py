from django.urls import path
from srinu1 import views
#from django.contrib import admin
urlpatterns = [
    #path(' ',admin.site.urls),
    path('hello/', views.hello, name='hello'), 
    path('srinu_data/',views.srinu_list,name='srinu_list'),
    path('index/',views.index,name = 'index'),
    path('srinuform/',views.srinuform,name='srinuform'),
    path('employee/',views.empform,name="employee"),
]