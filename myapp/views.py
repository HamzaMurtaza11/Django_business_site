from email import message
from multiprocessing import context
from os import name
from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import contact
from django.contrib import messages
# Create your views here.
def index(request):

  #context= {"variable1":"HamzaMurtaza", "variable2":"WelCoMe"} 
  #return HttpResponse("This is homepage")
  if request.method=="POST":
    name= request.POST.get('name')
    email=request.POST.get('email')
    message=request.POST.get('message')
    Contact= contact(name=name,email=email,message=message,date=datetime.today())
    Contact.save()
    messages.success(request, 'Your message has been sent.')


  


  return render(request, "index.html")


def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse("This is services page")



  