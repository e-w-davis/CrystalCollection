from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('crystals/', views.crystals_index, name='index'),
    path('crystals/<int:crystal_id>/', views.crystals_detail, name='detail'),
    path('crystals/create/', views.CrystalCreate.as_view(), name='crystals_create'),
    path('crystals/<int:pk>/update/', views.CrystalUpdate.as_view(), name='crystals_update'),
    path('crystals/<int:pk>/delete/', views.CrystalDelete.as_view(), name='crystals_delete'),
    path('crytals/<int:crystal_id>/add_cleansing/', views.add_cleansing, name='add_cleansing'),
    path('crystals/<int:crystal_id>/assoc_location/<int:location_id>/', views.assoc_location, name='assoc_location'),
    path('crystals/<int:crystal_id>/assoc_location/<int:location_id>/remove', views.assoc_location_remove, name='assoc_location_remove'),
    path('locations/', views.LocationList.as_view(), name='locations_index'),
    path('locations/<int:pk>/', views.LocationDetail.as_view(), name='location_detail'),
    path('locations/create/', views.LocationCreate.as_view(), name='locations_create'),
    path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='locations_delete')
]