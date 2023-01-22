from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        'variable':"this is send"
    }
    # messages.success(request, "this is a text message")
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, 'contact.html')
