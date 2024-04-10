from django.urls import path
from . import views

urlpatterns =[
    path('v1/getData/',views.getData),
    path('v1/addData/',views.addData)
]