from django.shortcuts import render, redirect
from rent.models import Customer, Rental
from faker import Faker 
from rent.forms import RentalAddForm
from django.contrib import messages

# Create your views here.
def cosmoter_fill_by_faker():
    fake = Faker()
    for _ in range(25):
        costom = Customer(first_name=fake.first_name(),last_name=fake.last_name(), email = fake.email(), phone_number = fake.phone_number(), adress = fake.address(), city = fake.city(),contry = fake.country())
        costom.save()
def add_rentall(request):
    if request.method == "POST":
        form = RentalAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Rental added !")
            return redirect('home')
        else:
            return render(request, 'rent/add_rental.html', {"form":form})
    else:
        form = RentalAddForm()
        return render(request, 'rent/add_rental.html', {"form":form})
def home(request):
    cust = Customer.objects.all()
    return render(request, "rent/home.html", {'customers': cust})