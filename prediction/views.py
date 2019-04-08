from django.shortcuts import render
from django.core import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import TemplateView
from .models import *
from .learning import * 
import json

class LandingView(TemplateView):
    template_name = 'extras/form_get.html'


class Evaluated(APIView):

    learn = Learning(3)

    def training(self):
        historics = Gender.objects.all()
        data = []
        for i in historics:
            data.append([i.height, i.weight, i.options])
        return data

    def post(self, request, *args, **kwargs):
        try:
            historic = self.training()
            if request.method == 'POST':
                result = self.learn.operation(historic, request.POST["height"])
                result_json = {'result': result}
                gender_reg = Gender(weight=request.POST["weight"], height=request.POST["height"], options=result)
                gender_reg.save()
                return Response(result_json)
        except Exception as e:
            print(e)
            return Response("Ha ocurrido un error!!!")