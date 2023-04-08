from django.urls import path,re_path
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("routing", views.routing, name="routing"),
    path("police", views.police, name="police"),
    path("cammera", views.cammera, name="cammera"),
    path("contact", views.contact, name="contact"),

    path("getLocation",views.get_location, name= "getLocation")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)