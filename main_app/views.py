from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
  return HttpResponse('ComplimentMyClothes Home Page')

class ClothingList(ListView):
    model = 

class ClothingDetail(DetailView):
    model = 
    pk_url_kwarg = "clothing_id"

class ClothingCreate(CreateView):
    model = 
    fields = '__all__'
    success_url = reverse_lazy('clothing_all')
    
class ClothingUpdate(UpdateView):
    model = 
    fields = '__all__'
    pk_url_kwarg = 'clothing_id'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('clothing_all')

class GameDelete(DeleteView):
    model = 
    pk_url_kwarg = 'clothing_id'
    success_url = reverse_lazy('clothing_all')