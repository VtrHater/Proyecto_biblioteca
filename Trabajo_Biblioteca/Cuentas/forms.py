from django import forms
from .models import Solicitudes
class solicitudesform(forms.ModelForm):

    class Meta:
        model = Solicitudes
        fields = '__all__'