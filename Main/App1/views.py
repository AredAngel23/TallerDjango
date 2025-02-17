from django.shortcuts import render, get_object_or_404
from .models import AutorDb, FraseDb

# Create your views here.
def IndexView(request):
    '''Home'''
    
    # Solicitamos los objetos a la base de datos y los ordenamos del último al primero
    autores = AutorDb.objects.all().order_by("-id")
    
    # retornamos una http con la plantilla index.html y los objetos de la base de datos
    return render(request, "index.html", {"autores":autores})

def AutorView(request, id):
    # Solicitamos un objeto a la base de datos y si no existe elevamos un 404
    autor = get_object_or_404(AutorDb, id=id)
    
    # retornamos una http con la plantilla autor.html y el objeto de la base de datos
    return render(request, "autor.html", {"autor":autor})