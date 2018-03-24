from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.views.generic.edit import DeleteView
from django.urls import reverse, reverse_lazy

from ModelExample.models import Contact

# Create your views here.

class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'

class CreateContactView(CreateView):
    model = Contact
    template_name = 'create_contact.html'
    fields = ['first_name', 'last_name']

    def get_success_url(self):
        return reverse('contacts-list')

class DeleteContactView(DeleteView):
    model = Contact
    template_name = 'contact_confirm_delete.html'
    success_url = reverse_lazy('contacts-list')



 
