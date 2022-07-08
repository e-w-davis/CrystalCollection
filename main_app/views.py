from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Crystal, Location
from .forms import CleansingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def crystals_index(request):
    crystals = Crystal.objects.all()
    return render(request, 'crystals/index.html', {'crystals': crystals})

def crystals_detail(request, crystal_id):
    crystal = Crystal.objects.get(id=crystal_id)
    loc_crystal_isnt = Location.objects.exclude(id__in = crystal.location.all().values_list('id'))
    cleansing_form = CleansingForm()
    return render(request, 'crystals/detail.html', {
        'crystal': crystal, 'cleansing_form': cleansing_form,
        'location': loc_crystal_isnt
    })

def add_cleansing(request, crystal_id):
    form = CleansingForm(request.POST)
    if form.is_valid():
        new_cleansing = form.save(commit=False)
        new_cleansing.crystal_id = crystal_id
        new_cleansing.save()
    return redirect('detail', crystal_id=crystal_id)

def assoc_location(request, crystal_id, location_id):
    Crystal.objects.get(id=crystal_id).location.add(location_id)
    return redirect('detail', crystal_id=crystal_id)

def assoc_location_remove(request, crystal_id, location_id):
    Crystal.objects.get(id=crystal_id).location.remove(location_id)
    return redirect('detail', crystal_id=crystal_id)

class CrystalCreate(CreateView):
    model = Crystal
    fields = '__all__'
    success_url = '/crystals/'

class CrystalUpdate(UpdateView):
    model = Crystal
    fields = ['family', 'hardness', 'color']

class CrystalDelete(DeleteView):
    model = Crystal
    success_url = '/crystals/'

class LocationList(ListView):
    model = Location
    template_name = 'locations/index.html'

class LocationDetail(DetailView):
    model = Location
    template_name = 'locations/detail.html'

class LocationCreate(CreateView):
    model = Location
    fields = '__all__'

class LocationDelete(DeleteView):
    model = Location
    success_url = '/locations/'