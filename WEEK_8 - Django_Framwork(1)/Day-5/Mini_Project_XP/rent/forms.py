from django.forms import ModelForm
from .models import Customer, Rental
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
class RentalForm(ModelForm):
    class Meta:
        model = Rental
        fields = "__all__"