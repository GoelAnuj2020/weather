import json
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import xml.etree.ElementTree as ET
from . import models as api_models


class Home(View):

    template_name = 'home.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(Home, self).dispatch(*args, **kwargs)
    def get(self, request):

        city_obj = api_models.City.objects.all()
        return render(request, self.template_name, {'city_obj': city_obj})

    def post(self, request):

        if request.POST.get('city_name'):
            city_obj = api_models.City.objects.filter(name=request.POST.get('city_name'))
            if not city_obj:
                city_obj = api_models.City(name=request.POST.get('city_name'))
                city_obj.save()
        city_obj = api_models.City.objects.all()
        return render(request, self.template_name, {'city_obj': city_obj})


class Weather(View):

    template_name = 'home.html'
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(Weather, self).dispatch(*args, **kwargs)
    def get(self, request):

        weather_url = 'http://api.openweathermap.org/data/2.5/weather?mode=xml&appid=2de143494c0b295cca9337e1e96b00e0&q=In,'
        city = request.GET.get('city')
        weather_url += city
        response = requests.get(weather_url)

        root = ET.fromstring(response.content)
        parameter = request.GET.get('parameter')
        result = None
        for child in root:
            print(child.tag, child.attrib)
            if child.tag == parameter:
                result = json.dumps(child.attrib)
                print result
                print type(result)
        return HttpResponse(result)

    def post(self, request):

        weather_url = 'http://api.openweathermap.org/data/2.5/weather?mode=xml&appid=2de143494c0b295cca9337e1e96b00e0&q=In,'
        city = request.GET.get('city')
        weather_url += city
        response = requests.get(weather_url)

        root = ET.fromstring(response.content)
        parameter = request.GET.get('parameter')
        result = None
        for child in root:
            print(child.tag, child.attrib)
            if child.tag == parameter:
                result = json.dumps(child.attrib)
                print result
                print type(result)
        return HttpResponse(result)