from django.urls import path, include
from . import views
from .views import ClothingList, ClothingCreate, ClothingDetail, ClothingUpdate, ClothingDelete, SearchResultsView, SearchWeatherView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search-by-weather/', SearchWeatherView.as_view(), name='search_weather_results'),
    path('clothing/', ClothingList.as_view(), name='clothing_all'),
    path('clothing/add/', ClothingCreate.as_view(), name='clothing_create'),
    path('clothing/<int:clothing_id>/', ClothingDetail.as_view(), name='clothing_detail'),
    path('clothing/<int:clothing_id>/update', ClothingUpdate.as_view(), name='clothing_update'),
    path('clothing/<int:clothing_id>/delete', ClothingDelete.as_view(), name='clothing_delete'),
    path('clothing/<int:clothing_id>/add_photo/', views.add_photo, name='add_photo'),
    path('photo/<int:pk>/delete', views.PhotoDeleteView.as_view(), name='photo-delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
