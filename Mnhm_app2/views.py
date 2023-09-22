from django.shortcuts import render
from django.http import HttpResponse

def vista_A_Dos(request):
    vC="""
        <h1>c</h1>
        """
    return HttpResponse(vC)

def vista_B_Dos(request):
    vD="""
        <h1>d</h1>

        """
    return HttpResponse(vD)