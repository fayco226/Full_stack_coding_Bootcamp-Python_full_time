from django.shortcuts import render, redirect
from .forms import CustomerForm
# from faker import Faker
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Customer, Vehicule, VehiculeSize, VehiculeType, Rental, RentalRate

from faker import Faker


# Create your views here.
def rentallist(request):
    rental = Rental.objects.all().order_by('rental_date')
    page = Paginator(rental, 5)
    pge = request.GET.get('page')
    cust = page.get_page(pge)
    return render(request, 'rent/rentallist.html', {'custom_page': cust})


def customer_fill_by_faker():
    fake = Faker()
    for _ in range(30):
        customer = Customer(first_name=fake.first_name(),
                            last_name=fake.last_name(),
                            email=fake.email(),
                            phone_number=fake.phone_number(),
                            address=fake.adress(),
                            city=fake.city(),
                            country=fake.country())
        customer.save()


def home(request, id=0):
    if id != 0:
        customer = Customer.objects.get(id=id).delete()
        return redirect("home")
    else:
        if request.method == "POST":
            customer = Customer.objects.all()
            form = CustomerForm(request.POST)
            page = Paginator(customer, 10)
            pge = request.GET.get('page')
            cust = page.get_page(pge)
            if form.is_valid():
                form.save()
                messages.success(request, "Customer added !")
                return redirect('home')
            else:
                return render(request, 'rent/home.html', {"form": form, 'custom_page': cust})
        else:
            form = CustomerForm()
            customer = Customer.objects.all()
            page = Paginator(customer, 5)
            pge = request.GET.get('page')
            cust = page.get_page(pge)

            return render(request, 'rent/home.html', {"form": form, 'custom_page': cust})
