from django.shortcuts import render
from django.http import HttpResponse

def vista_A_Dos(request):
    vC="""
        <h1 style="background:Gray">Este es el primero texto de la vista A de la segunda app</h1>
        <br>
        <br>
        <h2 style="background:green">Y el siguiente boton</h2>
        <br>
        <br>
        <h3 style="background:burlywood">Lo llevara a vista B de esta aplicacion 2</h3>
        <br>
        <br>
        <button><a href="../app2_vista2/">Ir a vista B de la app2</a></button>
        <br>
        <button><a href="../app1_vista1/">Ir a la primera app </a></button>
        """
    return HttpResponse(vC)

def vista_B_Dos(request):
    vD="""
        <h1 style="background:brown">Ahora esta en la vista B</h1>
        <br>
        <h2 style="background:greenyellow"> Con diferentes colores para que se vea la diferencia </h2>
        <br>
        <h3 style="background:gray">Si quiere volver a la vista A precione el boton</h3>
        <br>
        <button><a href="../app2_vista1/">Ir a vista A de la app2</a></button>
        <br>
        <button><a href="../app1_vista1/">Ir a la primera app </a></button>
        """
    return HttpResponse(vD)