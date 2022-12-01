from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Place
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def PlaceList(request):
    if request.method == 'GET':
        queryset = Place.objects.all()
        context = list(queryset.values('id', 'name'))
        return JsonResponse(context, safe=False)
    elif request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        measurement = Place()
        measurement.name = data_json['name']
        measurement.save()
        return HttpResponse("successfully created measurement")

