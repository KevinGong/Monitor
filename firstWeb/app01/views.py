from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from app01.models import *
# Create your views here.

def index(request):
    return render_to_response('index.html')
def account_login(request):
    print request.POST
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect("/dashboard/")
    else:
        return render_to_response('index.html',{'login_err':"Wrong username or password!"})
def logout(request):
    user = request.user
    auth.logout(request)
    return HttpResponse("<h3>User %s logout success!</h3>" % user)
def dashboard(request):
    #print request.user.username,request.user.password
    return render_to_response("dashboard.html",{'user':request.user})
def auto(request):
    ip_list = IP.objects.all()
    return render_to_response("auto.html",{'user':request.user,'ip_list':ip_list})
