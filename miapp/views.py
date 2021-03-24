from django.shortcuts import render, HttpResponse

# Create your views here.


def hola_mundo(request):
    return HttpResponse("""
    <h1>Hola Mundo</h1>
    <h3>Primeras rutas con Django</h3>
    """)
