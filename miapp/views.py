from django.shortcuts import render, HttpResponse

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


def hola_mundo(request):
    html = """
    <h1>Hola Mundo</h1>
    <h3>Primeras rutas con Django</h3>
    """
    return HttpResponse(layout+html)


def contact(request, nombre):
    html = f"Contacto {nombre}"
    return HttpResponse(layout+html)
