from django.shortcuts import render
from django.http import HttpResponse

def vista_A_Uno(request):
    
    vA="""
        <h1 style="background:yellow">Este es el primero texto de la vista A de la primera app</h1>
        <br>
        <br>
        <h2 style="background:green">Y el siguiente boton</h2>
        <br>
        <br>
        <h3 style="background:darkcyan">Lo llevara a vista B de esta aplicacion 2</h3>
        <br>
        <br>
        <button><a href="../app1_vista2/">Ir a vista B de esta primera app</a></button>
        <br>
        <button><a href="../app2_vista1/">Ir a la segunda app </a></button>
        """
    return HttpResponse(vA)


def vista_B_Uno(request):

    vB="""
        <h1 style="background:darkcyan">Ahora esta en la vista B de la primera app</h1>
        <br>
        <h2 style="background:yellow"> Con diferentes colores para que se vea la diferencia </h2>
        <br>
        <h3 style="background:grey">Si quiere volver a la vista A precione el boton</h3>
        <br>
        <button><a href="../app1_vista1/">Ir a vista A de esta primera app</a></button>
        <br>
        <button><a href="../app2_vista1/">Ir a la segunda app </a></button>
        """
    return HttpResponse(vB)