import folium
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,"Vigilantix/index.html")

def map(request):
    # Define the map center
    center = [27.030703, 75.893527]
    # Create the map using Folium
    m = folium.Map(location=center, zoom_start=16)
    # Add a marker to the map for the center
    location_name="Arya College of Enginnering, Kukas"
    tooltip = location_name
    folium.Marker(location=center, tooltip=tooltip).add_to(m)
    #return map 
    m=m._repr_html_() #updated
    context = {'my_map': m}
    return render(request, 'Vigilantix/map.html', context)