from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from members.models import Members
from django.contrib import messages

# Create your views here.

def index(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def members_data(request):
    var = {"first_name":"Chuchart","last_name":"Saetiew"}
    mData = Members()
    mData.firstname = "Name"
    mData.lastname = "Surname"
    try:
        mData.save()
        messages.success(request,"Complete!")
    except:
        messages.success(request,"Try again!")
    finally:
        return render(request,"myfirst.html",var)
    