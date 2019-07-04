from django.shortcuts import render

from .forms import RegForm

# Create your views here.
def inicio(request):
    form = RegForm(request.POST or None)
    print (dir(form)) #ver los metodos a utilizar del formulario
    if form.is_valid():
        print form.cleaned_data
        form_data = form.cleaned_data
        email = form_data.get("email")
        #print form_data.get("edad")
    context = {
        "el_form": form
    }
    return render(request, 'inicio.html', context)