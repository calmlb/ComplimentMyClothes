from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Clothing
from django.urls import reverse_lazy

# Create your views here.

def home(request):
  return render(request, 'home.html')

class ClothingList(ListView):
    model = Clothing

class ClothingDetail(DetailView):
    model = Clothing
    pk_url_kwarg = "clothing_id"

class ClothingCreate(CreateView):
    model = Clothing
    fields = '__all__'
    success_url = reverse_lazy('clothing_all')
    
class ClothingUpdate(UpdateView):
    model = Clothing
    fields = '__all__'
    pk_url_kwarg = 'clothing_id'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('clothing_all')

class ClothingDelete(DeleteView):
    model = Clothing
    pk_url_kwarg = 'clothing_id'
    success_url = reverse_lazy('clothing_all')

def about(request):
    return render(request, 'about.html')