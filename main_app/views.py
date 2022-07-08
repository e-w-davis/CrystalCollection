from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Crystal, Location
from .forms import CleansingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def crystals_index(request):
    crystals = Crystal.objects.filter(user=request.user)
    return render(request, 'crystals/index.html', {'crystals': crystals})

@login_required
def crystals_detail(request, crystal_id):
    crystal = Crystal.objects.get(id=crystal_id)
    loc_crystal_isnt = Location.objects.exclude(id__in = crystal.location.all().values_list('id'))
    cleansing_form = CleansingForm()
    return render(request, 'crystals/detail.html', {
        'crystal': crystal, 'cleansing_form': cleansing_form,
        'location': loc_crystal_isnt
    })

@login_required
def add_cleansing(request, crystal_id):
    form = CleansingForm(request.POST)
    if form.is_valid():
        new_cleansing = form.save(commit=False)
        new_cleansing.crystal_id = crystal_id
        new_cleansing.save()
    return redirect('detail', crystal_id=crystal_id)

@login_required
def assoc_location(request, crystal_id, location_id):
    Crystal.objects.get(id=crystal_id).location.add(location_id)
    return redirect('detail', crystal_id=crystal_id)

@login_required
def assoc_location_remove(request, crystal_id, location_id):
    Crystal.objects.get(id=crystal_id).location.remove(location_id)
    return redirect('detail', crystal_id=crystal_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class CrystalCreate(CreateView):
    model = Crystal
    fields = ['name', 'family', 'hardness', 'color']
    success_url = '/crystals/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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