from django.shortcuts import render
from django.http import HttpResponse

def vista_A_Uno(request):
    
    vA="""
        <h1>a </h1>   
    
    """
    return HttpResponse(vA)
