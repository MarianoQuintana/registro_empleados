from django.urls import path
from emp.views import index

urlpatterns=[
    path("index/", index),

]