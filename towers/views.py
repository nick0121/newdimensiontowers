from django.shortcuts import render
from .models import Towers, Images
from .forms import SearchForm
from django.shortcuts import redirect


# Create your views here.
################################# From index page no link parameter ############# Load all towers
def index(request):

    

    form = SearchForm()
    if request.method == "POST":
        selection = request.POST.get('tower_id')
        return redirect('tower_manufacturer', selection)
        
    else:
        towers = Towers.objects.all()


    title = "ALL NDT"

    context = {
        'towers': towers,
        'form': form,
        'title': title,
    }

    return render(request, 'towers/towers.html', context)



#################################################### Render from Index manufacturer selection passes tower_id to method
def tower_manufacturer(request, manufacturer_name):

    form = SearchForm()

    towers = Towers.objects.filter(manufacturer=manufacturer_name)

    if towers:
        pass
    else:
        towers = Towers.objects.filter(manufacturer="ndt")


    title = towers[0].get_name()

    context = {
        'towers': towers,
        'form': form,
        'title': title,
    }
    

    return render(request, 'towers/towers.html', context)


#################################################### Render from towers page passes manufacturer name and boat id
def tower_product(request, manufacturer_name, boat_id):

    tower = Towers.objects.filter(slug=boat_id)
    tower_id = tower[0].id

    images = Images.objects.filter(tower_id=tower_id)
    
    context = {
        'tower': tower,
        "images": images,
    }

    return render(request, 'pages/product.html', context)