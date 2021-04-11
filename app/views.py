from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q

def index(request):
    images = Image.objects.all()

    query = request.GET.get('q')
    if query:
        images = Image.objects.filter(
            Q(title__icontains=query) 
        )
    context = {
        'images': images
    }
    return render(request, 'index.html', context)
    

def gallery(request):

    category = request.GET.get('category')
    if category == None:
        images = Image.objects.all()
    else:
        images = Image.objects.filter(category__name=category)

    
    categories = Category.objects.all()

    query = request.GET.get('q')
    if query:
        images = Image.objects.filter(
            Q(title__icontains=query)
        )
    context = {
        'images': images
    }

    context = {
        'categories': categories,
        'images': images,
    }
    return render(request, 'gallery.html', context)

# def addPhoto(request):
    categories = Category.objects.all()
    locations = Location.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        if data['location'] != 'none':
            location = Location.objects.get(id=data['location'])
        elif data['location_new'] != '':
            location, created = Location.objects.get_or_create(name=data['location_new'])
        else:
            location = None

        image = Image.objects.create(
            category=category,
            location=location,
            description=data['description'],
            title=data['title'],
            image=image,
        )

        return redirect('gallery')


    context = {
        'categories': categories,
        'locations': locations,
    }
    return render(request, 'addPhoto.html', context)
