from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Crystal:
    def __init__(self, name, family, hardness, color):
        self.name = name
        self.family = family
        self.hardness = hardness
        self.color = color

crystals = [
    Crystal('Amethyst', 'Quartz', 7, 'Purple'),
    Crystal('Ruby', 'Beryl', 9, 'Red'),
    Crystal('Diamond', 'Carbon-silicon', 10, 'Clear'),
    Crystal('Labradorite', 'Feldspar', 6, 'Multicolored'),
    Crystal('Fire Opal', 'Silicates Quartz', 6, 'Orange'),
]

def crystals_index(request):
    return render(request, 'crystals/index.html', {'crystals': crystals})