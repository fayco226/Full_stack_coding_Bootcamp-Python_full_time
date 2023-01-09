from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    phone_number  = PhoneNumberField()
    adress = models.CharField( max_length=50)
    city = models.CharField( max_length=50)
    contry = models.CharField(max_length=50)

   
    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name','last_name'] 
    
    
    

class VehiculeType(models.Model):
    name = models.CharField(max_length=50)
    
    def _str_(self):
        return self.name
    
    
    
    
class VehiculeSize(models.Model):
    name = models.CharField(max_length=50)
    
    def _str_(self):
        return self.name
    
    
    
    
    
class Vehicule(models.Model):
    vehicule_type = models.ForeignKey(VehiculeType, related_name=("Type"), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.FloatField()
    vehicule_size = models.ForeignKey(VehiculeType, related_name=("Size"), on_delete=models.CASCADE)
    
    def _str_(self):
        return self.vehicule_type
    
    
class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now_add = True,null=True )
    client = models.ForeignKey(Customer, related_name=("Client"), on_delete=models.CASCADE)
    vehicule = models.ForeignKey(Vehicule, related_name=("Vehicule"), on_delete=models.CASCADE)
    
    
    class Meta:
        ordering = ['rental_date']
    
    
    
class RentalRate(models.Model):
    dayli_rate = models.FloatField()
    vehicule_type = models.ForeignKey(VehiculeType, on_delete=models.CASCADE)
    vehicule_size = models.ForeignKey(VehiculeSize, on_delete=models.CASCADE)
