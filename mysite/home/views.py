from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("This is home Page")
    return render(request,"index.html")

def about(request):
    # return HttpResponse("This is about Page")
    return render(request,"about.html")

def services(request):
    # return HttpResponse("This is about Services")
    return render(request,"services.html")

def contact(request):
    # return HttpResponse("This is about Contact Page")
    
    return render(request,"contact.html")
