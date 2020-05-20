from django.forms import ModelForm
from .models import Order

#create the form class
class orderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'