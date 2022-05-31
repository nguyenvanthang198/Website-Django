from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.db.models import Q
# Create your views here.
from .models import *
# from PortalMgmt.views import DefaultContext as dContext


def Index(request):
    context = {}
    # all_about = AboutContent.objects.all()
    # context['all_about'] = all_about
    template = loader.get_template(str('Cart/index.html'))
    return HttpResponse(template.render(context, request))


from django.shortcuts import render

# Create your views here.
