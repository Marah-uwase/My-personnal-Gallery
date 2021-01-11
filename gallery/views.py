from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Location,Category


# Create your views here.
def photos_of_day(request):
    date = dt.date.today()
    photos = Image.objects.all()
    locations = Location.objects.all()
    category = Category.objects.all()
   
    # elif 'category' in request.GET and request.GET['category']:
    #     cat = request.GET.get('categories')
    #     images = Image.view_category(cat)
    #     return render(request, 'all_photos/today_photos.html', {"name":name,"images":images,"cat":cat })
      
    return render(request, 'all_photos/today_photos.html', {"date": date, "photos": photos, "locations": locations})      

def search_results(request):
    '''
    search function to display search search_results
    args:
    order defines category
    '''
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all_photos/search.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_photos/search.html', {"message": message})
def location(request,location):
    locations = Location.objects.all()
    selected_location = Location.objects.get(id = location)
    images = Image.objects.filter(location = selected_location.id)
    return render(request, 'all_photos/location.html', {"location":selected_location,"locations":locations,"images":images})