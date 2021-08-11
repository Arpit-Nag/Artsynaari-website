from django import forms
from .models import ProductRequest

class RequestForm(forms.ModelForm):
    class Meta():
        model = ProductRequest
        fields = ('local_address','discription','city','size',
        'district','state','pin','contact')
        widgets={
            'discription':forms.Textarea()

        }
