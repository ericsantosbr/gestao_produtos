from django.forms import ModelForm
from home.models import Product


class EditProduct(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'photo']