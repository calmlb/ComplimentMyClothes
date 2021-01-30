from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Clothing
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
  error_message=""
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('clothing')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required 
def Clothing(request):
    clothing = Clothing.objects.all()
    clothing = Clothing.objects.filter(user=request.user)
    return render(request, 'home')
    
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