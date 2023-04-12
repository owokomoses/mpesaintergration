from django.shortcuts import render
from django_daraja.mpesa import utils
from django.http import HttpResponse,JsonResponse
from django.views.generic import View
from django_daraja.mpesa.core import MpesaClient
from decouple import config
from datetime import datetime

def Home(request):
    return render(request,'index.html')