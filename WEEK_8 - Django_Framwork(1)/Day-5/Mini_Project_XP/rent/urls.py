from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home0, name="home0" ),
    path('rent/customer/',views.home, name='home'),
    path('rent/customer/<id>', views.home, name="detailCustomer"),
    path('rent/customer/add', views.addCustomer, name="addCustomer"),
    path('rent/rental/', views.rentallist, name="rentallist" ),
    path('rent/rental/add', views.addRental, name="addRental"),
    path('rent/rental/<id>', views.rentallist, name="detailRental"),
    path('rent/vehicule/', views.rentallist, name="rentallist" ),
    path('rent/vehicule/add', views.addRental, name="addRental"),
    path('rent/vehicule/<id>', views.rentallist, name="detailRental"),

]