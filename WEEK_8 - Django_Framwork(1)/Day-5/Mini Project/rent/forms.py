from django.forms import ModelForm
from rent.models import Rental
class RentalAddForm(ModelForm):
    class meta:
        model : Rental
        fields: "__all__"