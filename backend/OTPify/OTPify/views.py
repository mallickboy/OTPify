from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hellow World Django")
    return render(request=request, template_name="website/index.html")

def about(request):
    return HttpResponse("About page")

def contact(request):
    return HttpResponse("Contact contact@mallickboy.com")