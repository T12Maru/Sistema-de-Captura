from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Dengue
# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password'] == request.POST['confirmP']:
            try:
                #registrando un usuario
                user = User.objects.create_user(username=request.POST['usuario'],password=request.POST['password'])
                user.save()
                login(request,user)
                return redirect('inicio')
            except IntegrityError:
                return render(request,'signup.html',{
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request,'signup.html',{
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


def signin(request):

    if request.method =='GET':    
        return render(request,'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request,username=request.POST['usuario'],password=request.POST['password'])
        if user is None:
            return render(request,'signin.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request,user)
            return redirect('inicio')

def grafico(request):
    if request.user.is_authenticated:
        numMujeres = []
        numMujeres.append(Dengue.objects.filter(entidad_res="26").filter(sexo="2").filter(municipio_res="030").count())
        numMujeres.append(Dengue.objects.filter(entidad_res="26").filter(sexo="2").filter(municipio_res="018").count())
        numMujeres.append(Dengue.objects.filter(entidad_res="26").filter(sexo="2").filter(municipio_res="043").count())
        numMujeres.append(Dengue.objects.filter(entidad_res="26").filter(sexo="2").filter(municipio_res="029").count())
        numMujeres.append(Dengue.objects.filter(entidad_res="26").filter(sexo="2").filter(municipio_res="042").count())

        numHombres = []
        numHombres.append(Dengue.objects.filter(entidad_res="26").filter(sexo="1").filter(municipio_res="030").count())
        numHombres.append(Dengue.objects.filter(entidad_res="26").filter(sexo="1").filter(municipio_res="018").count())
        numHombres.append(Dengue.objects.filter(entidad_res="26").filter(sexo="1").filter(municipio_res="043").count())
        numHombres.append(Dengue.objects.filter(entidad_res="26").filter(sexo="1").filter(municipio_res="029").count())
        numHombres.append(Dengue.objects.filter(entidad_res="26").filter(sexo="1").filter(municipio_res="042").count())

        dengueEstados =[]
        dengueEstados.append(Dengue.objects.filter(entidad_res="26").count() )
        dengueEstados.append(Dengue.objects.filter(entidad_res="25").count() )
        dengueEstados.append(Dengue.objects.filter(entidad_res="02").count() )
        dengueEstados.append(Dengue.objects.filter(entidad_res="07").count() )
        
        return render(request,'grafico.html',{'numMujeres': numMujeres,
                                              'numHombres': numHombres,
                                              'dengueEsta': dengueEstados
            })
    else:
        return redirect('signin')
    
def inicio(request):
    if request.user.is_authenticated:
        return render(request,"inicio.html")
    else:
        return redirect('signin')

def signout(request):
    logout(request)
    return redirect('signin')