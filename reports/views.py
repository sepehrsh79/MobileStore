from django.shortcuts import render
from mobiles.models import Mobile
from django.core import serializers
from django.db.models import F
from django.http import JsonResponse
import json

def report1(request):

    #filter a query with brand_nationality == Korea
    korean_mobiles = Mobile.objects.filter(brand_nationality="Korea")
    serialized_mobiles = serializers.serialize("json", korean_mobiles)
    return JsonResponse(serialized_mobiles, safe=False)

def report2(request,*args, **kwargs):
    
    #filter a query with input model name
    selected_model = request.GET.get("q")
    models = Mobile.objects.filter(brand_name=selected_model)
    serialized_mobiles = serializers.serialize("json", models)
    return JsonResponse(serialized_mobiles, safe=False)

def report3(request):

    #filter a query with brand_nationality == manufacturer
    mobiles = Mobile.objects.filter(brand_nationality=F('manufacturer'))
    serialized_mobiles = serializers.serialize("json", mobiles)
    return JsonResponse(serialized_mobiles, safe=False)
