from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
# Create your views here.

def index(request):
    return render_to_response('index.html')
