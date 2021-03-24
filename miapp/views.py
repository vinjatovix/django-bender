from django.shortcuts import render, HttpResponse, redirect, render

# Create your views here.


def index(request):

    return render(request, "index.html")


def hola_mundo(request, redir=0):

    if redir == 1:
        # return redirect('/contact')
        # si en vez del path usamos el nombre siempre funcionara aunque cambiemos el path mas adelante
        return redirect('contact', nombre="pepe", apellido="loco")

    return render(request, 'hola_mundo.html')


def contact(request, nombre="pablo", apellido="viña"):

    # por culpa de los valores por defecto solo se ejecutara el primer caso
    if nombre and apellido:
        html = f"<p>{nombre} {apellido}</p>"
    elif nombre:
        html = f"<p>{nombre}</p>"
    else:
        html = "No hay contacto"

    return HttpResponse(layout+html)
