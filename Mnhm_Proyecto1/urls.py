"""
URL configuration for Mnhm_Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Mnhm_app1 import views as v1
from Mnhm_app2 import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1_vista1/',v1.vista_A_Uno),
    path('app1_vista2/',v1.vista_B_Uno),
    path('app2_vista1/',v2.vista_A_Dos),
    path('app2_vista2/',v2.vista_B_Dos)
]
