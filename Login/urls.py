from django.urls import path
from . import views

urlpatterns=[
    path('User/',views.fnUser),
    path('Details/',views.fnDetails)
]