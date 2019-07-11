from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado

# Create your views here.
def inicio(request):
    titulo = "Hola Juli"

    if request.user.is_authenticated():
        titulo = "Bienvenido %s" %(request.user)

    form = RegModelForm(request.POST or None)
    context = {
            "el_titulo": titulo,
            "el_form": form
        }

    print (dir(form)) #ver los metodos a utilizar del formulario
    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.nombre:
            instance.nombre = "No declara nombre"
        form.save()

        context = {
            "el_titulo": "Gracias %s!" %(instance.nombre)
        }
        print(instance)
        print(instance.timestamp)

        #print(form.cleaned_data)
        #form_data = form.cleaned_data
        #emailForm = form_data.get("email")
        #nombreForm = form_data.get("nombre")
        #obj = Registrado.objects.create(email=emailForm, nombre=nombreForm)
        
        #registrado = Registrado()
        #registrado.email = emailForm
        #registrado.save()
    
    return render(request, 'inicio.html', context)

def contacto(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key, value in form.cleaned_data.items():
            print(key, value)

        form_email = form.cleaned_data.get("email")
        form_nombre = form.cleaned_data.get("nombre")
        form_mensaje = form.cleaned_data.get("mensaje")

        email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)

        send_mail(
            'Formulario de Contacto',
            email_mensaje,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
    context = {
        "form": form
    }
    return render(request, "contacto.html", context)