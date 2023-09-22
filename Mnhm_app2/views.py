from django.shortcuts import render
from django.http import HttpResponse

def vista_A_Dos(request):
    vC="""
        <h1>c</h1>
        """
    return HttpResponse(vC)
