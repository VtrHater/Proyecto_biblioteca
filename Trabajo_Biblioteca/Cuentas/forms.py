from django import forms
from .models import Solicitudes
from .models import Profile
from django.contrib.auth.models import User
from .models import Notification


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
        self.fields['autor'].disabled = True
        self.fields['fecha_publicación'].disabled = True
        self.fields['número_de_sistema'].disabled = True
        self.fields['ubicación'].disabled = True
        self.fields['departamento'].disabled = True
        self.fields['nota'].disabled = False
        self.fields['plazo'].disabled = True
        self.fields['funcionario'].disabled = True
        self.fields['prioridad'].disabled = True

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['telefono', 'departamento', 'imagen']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class NotificationForm(forms.ModelForm):
    usuarios = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=True,
        label="Seleccionar Funcionarios"
    )
    class Meta:
        model = Notification
        fields = ['usuarios', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu notificación'}),
        }