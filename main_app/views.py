from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Clothing
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class ClothingCreate(LoginRequiredMixin, CreateView):
  model = Clothing
  fields = '__all__'
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the photo
    # Let the CreateView do its job as usual
    return super().form_valid(form)
  success_url = reverse_lazy('clothing_all')

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
      return redirect('clothing_all')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
  clothing = Clothing.objects.filter(user=request.user)
  return render(request, 'home.html')

class ClothingList(ListView):
    model = Clothing
    template_name = 'clothing_all'

# @login_required 
# def clothing_user(request):
#   clothing = Clothing.objects.filter(user=request.user)
#   return render (request, 'main_app/clothing_detail.html', {'clothing_all': clothing_all})
    

class ClothingDetail(DetailView):
    model = Clothing
    pk_url_kwarg = "clothing_id"

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