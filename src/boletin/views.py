from django.shortcuts import render

from .forms import RegForm, RegModelForm


def inicio(request):
    titulo = "hola"
    if request.user.is_authenticated:
        titulo = "Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)
    
    context = {
                "titulo": titulo,
                "el_form": form,
            }

    if form.is_valid():
        instance = form.save(commit=False)
        nombre = form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        if not instance.nombre:
            instance.nombre = "persona"
        instance.save()

        context = {
            "titulo" : "gracias %s!" %(nombre)
        }
        print (instance)
        print (instance.timestamp)

    
    return render(request, "inicio.html", context)