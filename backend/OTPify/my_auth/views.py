from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
async def auth_page(request):
    return render(request=request, template_name="my_auth/auth.html")

async def order(request):
    return HttpResponse("inside my_auth/order")