import email
from email import message
from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request,"app/index.html")
def contact(request):
    n=request.POST.get("name")
    e=request.POST.get("email")
    m=request.POST.get("message")
    if(n and e and m):
        contactcls.objects.create(name=n,email=e,message=m)
        return render(request,"app/message.html")
    return render (request,"app/contact.html")
    
