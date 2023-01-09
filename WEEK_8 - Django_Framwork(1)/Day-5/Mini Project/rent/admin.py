from django.contrib import admin
from rent.models import Customer, VehiculeType, VehiculeSize, Vehicule, Rental, RentalRate
# Register your models here.
admin.site.register(Customer)
admin.site.register(VehiculeType)
admin.site.register(VehiculeSize)
admin.site.register(Vehicule)
admin.site.register(Rental)
admin.site.register(RentalRate)