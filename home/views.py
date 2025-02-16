from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages # it has 5 types of messages: debug, info, success, warning, error inbuilt in django

# Create your views here.
def index(request):
    context = {            # set of varaibles that are sent to the template
        'variable': 'this is sent'
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage") 

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":    # logic for saving data in database
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        if not name or not email or not phone or not desc:
            messages.error(request, "All fields are required!")  # Show error message
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()
            messages.success(request, "Your message has been sent!")  # Success message
    return render(request, 'contact.html')