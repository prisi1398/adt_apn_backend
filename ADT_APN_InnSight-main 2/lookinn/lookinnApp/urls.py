from django.urls import path
from . import views
from .views import delete_property
from .views import update_listing

urlpatterns=[
    path('getListings', views.getListings, name="jsondata"),
    path('cities/', views.list_cities, name='city-list'),
    path('city/<str:city>/listings/', views.city_listings, name='city-listings'),
    path('listingsdetails/<int:listing_id>/', views.listing_details, name='listing_details'),
    path('addListings/', views.addListings, name="jsondata"),
    path('deletelistings/<int:listing_id>/', delete_property, name='delete_property'),
    path('updatelistings/update/<int:listing_id>/', update_listing, name='update_listing'),


]