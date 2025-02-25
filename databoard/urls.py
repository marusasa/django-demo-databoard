from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getdata/<str:datatype>/<str:inputDate>/<str:duration>/", views.getdata, name="getdata"),
]