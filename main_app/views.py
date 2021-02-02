from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Clothing, Photo
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import uuid
import boto3
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'cmc-4'

class ClothingCreate(LoginRequiredMixin, CreateView):
  model = Clothing
  fields = '__all__'
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)
  success_url = reverse_lazy('clothing_all')

def signup(request):
  error_message=""
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('clothing_all')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def home(request):
  # clothing = Clothing.objects.all()
  # clothing = Clothing.objects.filter(user=request.user)
  return render(request, 'home.html')

class ClothingList(ListView):
    model = Clothing
    template_name = 'clothing_all'
    
    def get_queryset(self):
      if self.request.user.is_authenticated:
        return Clothing.objects.filter(user=self.request.user)
      else:
        return Clothing.objects.none()

@login_required 
def clothing_user(request):
  clothing = Clothing.objects.filter(user=request.user)
  return render (request, 'main_app/clothing_detail.html', {'clothing_all': clothing_all})

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

def add_photo(request,  clothing_id):
# photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
      s3 = boto3.client('s3')
      # need a unique "key" for S3 / needs image file extension too
      key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
      # just in case something goes wrong
      try:
          s3.upload_fileobj(photo_file, BUCKET, key)
          # build the full url string
          url = f"{S3_BASE_URL}{BUCKET}/{key}"
          # we can assign to clothing_id or clothing (if have clothing object)
          photo = Photo(url=url, clothing_id=clothing_id)
          photo.save()
      except:
          print('An error occurred uploading file to S3')
  return redirect('clothing_detail', clothing_id=clothing_id)

@method_decorator(login_required, name='dispatch')
class PhotoDeleteView(DeleteView):
    model = Photo
    fields = ('__all__')
    success_url = reverse_lazy('clothing_all')
    def get_success_url(self):
    return reverse_lazy('clothing_all')

class SearchResultsView(ListView):
    model = Clothing
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Clothing.objects.filter(
            Q(name__icontains=query) | Q(color__icontains=query)
        )
        return object_list
