from django import forms

from .models import Registrado
class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre", "email"]
    
    def clean_email(self):
        print(self.cleaned_data)
        emailForm = self.cleaned_data.get("email")
        email_base, email_proveedor = emailForm.split("@")
        email_dominio, email_extension = email_proveedor.split(".")
        if not "edu" in email_extension:
            raise forms.ValidationError("Por favor ingrese un correo edu")
        return emailForm
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        return nombre

class ContactForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)