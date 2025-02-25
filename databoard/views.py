from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
import json
import datetime
from datetime import date
from .models import Humidity, Temperature, BarometricPressure

def index(request):
    context = {}
    return render(request, "databoard/index.html", context)
    return HttpResponse("Hello, world. You're at the databoard index.")
    
def getdata(request,datatype, inputDate, duration):
    print(datatype)
    print(inputDate)
    print(duration)
    days = 7
    match duration:
        case '1d':
            days = 1
        case '5d':
            days = 5
        case '1w':
            days = 7
        case '2w':
            days = 14
        case '1m':
            days = 31
    match datatype:
        case 'humidity':
            return __getdataHumidity(inputDate,days)        
        case 'temperature':
            return __getdataTemperature(inputDate,days)
        case 'pressure':
            return __getdataPressure(inputDate,days)
        case _:
            return JsonResponse(json.dumps([]), safe=False)
        
        
        
def __getdataHumidity(inputDate, days):
    start_date = date.fromisoformat(inputDate)
    end_date = start_date + datetime.timedelta(days=days)
    print(start_date)
    print(end_date)
    queryset = Humidity.objects.filter(timestamp__range=(start_date, end_date))
    data = []
    for item in queryset:
        obj = {}
        obj['datetm'] = item.timestamp.strftime("%Y-%m-%d %H:%M")
        obj['val'] = item.humidity
        data.append(obj)        
    return JsonResponse(json.dumps(data), safe=False)

def __getdataTemperature(inputDate, days):
    start_date = date.fromisoformat(inputDate)
    end_date = start_date + datetime.timedelta(days=days)
    print(start_date)
    print(end_date)
    queryset = Temperature.objects.filter(timestamp__range=(start_date, end_date))
    data = []
    for item in queryset:
        obj = {}
        obj['datetm'] = item.timestamp.strftime("%Y-%m-%d %H:%M")
        obj['val'] = item.temperature
        data.append(obj)        
    return JsonResponse(json.dumps(data), safe=False)
    
def __getdataPressure(inputDate, days):
    start_date = date.fromisoformat(inputDate)
    end_date = start_date + datetime.timedelta(days=days)
    print(start_date)
    print(end_date)
    queryset = BarometricPressure.objects.filter(timestamp__range=(start_date, end_date))
    data = []
    for item in queryset:
        obj = {}
        obj['datetm'] = item.timestamp.strftime("%Y-%m-%d %H:%M")
        obj['val'] = item.pressure
        data.append(obj)        
    return JsonResponse(json.dumps(data), safe=False)