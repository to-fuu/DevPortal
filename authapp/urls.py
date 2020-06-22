from django.urls import path, include
from restapi.views import current_profile
from . import views

urlpatterns = [
    path('',  include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('profile/', current_profile, name="current_profile"),

]
