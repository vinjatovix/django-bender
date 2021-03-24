from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layout = """
<h1>Simple Django Demo</h1>
<hr/>
<ul>
    <li><a href="/">Home</a></li>
    <li><a href="/hola-mundo">Hola mundo</a></li>
    <li><a href="/contact">Contacto</a></li>
    <li><a href="/projects">Projects</a></li>
</ul>
"""


def index(request):

    html = """
    <h1>Home</h1>
    <p>Welcome</p>
    """
    return HttpResponse(layout+html)


def hola_mundo(request, redir=0):

    if redir == 1:
        # return redirect('/contact')
        # si en vez del path usamos el nombre siempre funcionara aunque cambiemos el path mas adelante
        return redirect('contact', nombre="pepe", apellido="loco")

    html = """
    <h1>Hola Mundo</h1>
    <h3>Primeras rutas con Django</h3>
    """
    return HttpResponse(layout+html)


def contact(request, nombre="pablo", apellido="viña"):

    # por culpa de los valores por defecto solo se ejecutara el primer caso
    if nombre and apellido:
        html = f"<p>{nombre} {apellido}</p>"
    elif nombre:
        html = f"<p>{nombre}</p>"
    else:
        html = "No hay contacto"

    return HttpResponse(layout+html)
