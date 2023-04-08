import folium
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from math import radians, cos, sin, asin, sqrt
from django.http import JsonResponse
# from django.http import *
from .models import PolicStation

def index(request):
    return render(request,"Vigilantix/index.html")

def search(request):
    latitude = 27.030703
    longitude = 75.893527
    radius = 5
    # Define the map center
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        radius = int(request.POST.get('radius'))
    else:
        latitude = 27.030703
        longitude = 75.893527
        radius = 5 
    center = [latitude, longitude]

    #creating map
    m = folium.Map(location=center, zoom_start=16)

    #adding user to map
    tooltip = "Your Location"
    icon=folium.Icon(color='red', prefix='fa', icon='user')
    folium.Marker(location=center, tooltip=tooltip, icon=icon).add_to(m)
    folium.Circle(
        location=center,
        radius=5*1000,
        fill=True,
        fill_opacity=0.1,
        color='green'
    ).add_to(m)

    # center = (stations[0].latitude, stations[0].longitude)
    #adding polic stations to map
    stations = PolicStation.objects.all()
    radius = radius  # radius in kilometers
    for station in stations:
        station_latitude = station.latitude
        station_longitude = station.longitude
        dist = haversine(latitude, longitude,station_latitude, station_longitude)
        if dist <= radius:
            marker_location = (station_latitude, station_longitude)
            tooltip = station.name
            icon=folium.Icon(color='blue', prefix='fa',icon='shield')
            folium.Marker(location=marker_location, tooltip=tooltip, icon=icon).add_to(m)


    m=m._repr_html_() #updated
    context = {'my_map': m,
               'latitudef':latitude,
               'longitudef':longitude
               }
    return render(request, 'Vigilantix/map.html', context)

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def get_location(request):
    if request.method == 'POST':
        # Extract the position data from the request body
        data = json.loads(request.body.decode('utf-8'))
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        print(latitude, longitude, data)

        # Do something with the position data
        # ...
        
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})\
            
def police(request):
     return render(request, 'Vigilantix/police.html')


def cammera(request):
     return render(request, 'Vigilantix/cammera.html')


def contact(request):
     return render(request, 'Vigilantix/contact.html')
