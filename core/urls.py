from django.contrib import admin
from django.urls import path, include

from api import views
from tickets import views as ticket_views


urlpatterns = [
    #path('',views.home,name='home'),
    #path('api/',include('api.urls')),
    path('',ticket_views.home,name='home'),
]
