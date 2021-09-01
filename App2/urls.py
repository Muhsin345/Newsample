from django.urls import path
from . import views

urlpatterns=[
    path('Sample2',views.fnName2),
    path('Name2',views.fnName3),
    path('Home',views.fnHome),
    path('Data1/',views.fnData),
   # path('Login',views.fnLogin)
]