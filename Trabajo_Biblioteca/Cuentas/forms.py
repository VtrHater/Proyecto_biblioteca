from django import forms
from .models import Solicitudes

class solicitudesform(forms.ModelForm):

    class Meta:
        model = Solicitudes
        fields = '__all__'

     

class estadosSolicitudesform(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(estadosSolicitudesform, self).__init__(*args, **kwargs)
    # Disable the 'estado' field (or any other field you want)
        self.fields['documento'].disabled = True
        self.fields['departamento'].disabled = True
        self.fields['nota'].disabled = False
        self.fields['autor'].disabled = True

