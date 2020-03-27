from django import forms
from .models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'variable',
            'value',
            'unit',
            'place',
            #'dateTime',
        ]

        labels = {
              'variable' : 'Producto',
             'value' : 'Precio',
             'unit' : 'Cantidad',
             'place' : 'Tienda',
            #'dateTime' : 'Date Time',
        }
