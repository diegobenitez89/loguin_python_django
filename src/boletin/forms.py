from django import forms

from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre","email"]

        def clean_email(self):
            email = self.cleaned_data.get("email")
            return email

        def clean_nombre(self):
            nombre = self.cleaned_data.get("nombre")
            # validaciones
            return nombre

class RegForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
