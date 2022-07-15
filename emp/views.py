from django.shortcuts import render
from emp.models import Datos_personales

def index(request):
    
    if request.GET:
        nombre = request.GET.get("nombre")
        edad = request.GET.get("edad")
        sexo = request.GET.get("sexo")
        domicilio = request.GET.get("domicilio")    
        tel = request.GET.get("tel")
        email = request.GET.get("email")
        print("------------------------------")
        dato = Datos_personales(nombre=nombre, edad=edad, sexo=sexo, domicilio=domicilio, tel=tel, email=email)
        dato.save()


    return render(request, "emp/index.html", {}) 

    

