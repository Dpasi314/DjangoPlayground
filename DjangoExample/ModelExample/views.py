from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from ModelExample.models import Contact

# Create your views here.

class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'

