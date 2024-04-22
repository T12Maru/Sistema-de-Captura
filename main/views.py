<<<<<<< HEAD
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
=======
from django.shortcuts import render
>>>>>>> f3eb7c58c0a32e862e79d0c5ad3b78e85c0fa09d

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
<<<<<<< HEAD
    if request.method =='GET':    
        return render(request,'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'signin.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            #login(request,user)
            return redirect('inicio')

def inicio(request):
    return render(request,'inicio.html')

def signout(request):
    logout(request)
    return redirect('signin')
=======
    return render(request,'signin.html')
>>>>>>> f3eb7c58c0a32e862e79d0c5ad3b78e85c0fa09d
