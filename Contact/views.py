from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Create your views here.
from .models import *
from Home.views import IndexViewContext as dContext
from Home.models import *


def IndexView(request):
    context = dContext()

    email = CompanyEmail.objects.all()
    context['email'] = email

    address = CompanyAddress.objects.all()
    context['address'] = address

    phone = CompanyPhone.objects.all()
    context['phone'] = phone

    data = request.POST

    print(request.POST)

    new_obj = ContactMessage()
    if 'name' in data:
        new_obj.name = data['name']
        if 'email' in data: new_obj.email = data['email']
        if 'subject' in data: new_obj.subject = data['subject']
        if 'content' in data: new_obj.content = data['content']
        new_obj.save()

    template = loader.get_template(str('Contact/index.html'))
    return HttpResponse(template.render(context, request))

def ContactMessage_Create(request):
    context = dContext()
    data = request.POST

    print(request.POST)

    new_obj = ContactMessage()
    if 'name' in data:
        new_obj.name = data['name']
        if 'email' in data: new_obj.email = data['email']
        if 'subject' in data: new_obj.subject = data['subject']
        if 'content' in data: new_obj.content = data['content']
        new_obj.save()

    template = loader.get_template(str('Contact/index.html'))
    return HttpResponse(template.render(context, request))
