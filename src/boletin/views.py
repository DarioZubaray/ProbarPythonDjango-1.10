from django.shortcuts import render

from .forms import RegForm
from .models import Registrado

# Create your views here.
def inicio(request):
    form = RegForm(request.POST or None)
    print (dir(form)) #ver los metodos a utilizar del formulario
    if form.is_valid():
        print(form.cleaned_data)
        form_data = form.cleaned_data
        emailForm = form_data.get("email")
        nombreForm = form_data.get("nombre")
        obj = Registrado.objects.create(email=emailForm, nombre=nombreForm)
        
        #registrado = Registrado()
        #registrado.email = emailForm
        #registrado.save()
    context = {
        "el_form": form
    }
    return render(request, 'inicio.html', context)
    