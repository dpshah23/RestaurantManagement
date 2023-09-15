from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index(request):
    if 'user' in request.session:
        b=register.objects.get(email=request.session['user'])
    a=Restaurant.objects.all()
    return render(request,'index.html',{'res':a})

def register(request):
    if request.method == 'POST':
        a = Register()
        a.name=request.POST['name']

        a.email = request.POST['email']
     
        a.contact = request.POST['contact']
       
        a.address=request.POST['address']
    
        a.password = request.POST['password']

        
        c=Register.objects.filter(password=request.POST['password'])
        
       
     
        b=Register.objects.filter(email=request.POST['email'])
        if len(b)==0:
            a.save()
            return render(request,'register.html')
        else:
             return render(request,'register.html',{'already':"Email Already Exists"})
            
    else:

        return render(request,'register.html')



def login(request):
    if request.method=='POST':

        a=Register.objects.get(email=request.POST('email'))
        if request.POST['password']==a.password:
            request.session['user']==a.email

            return redirect('index')
        else:

          return render(request,'login.html')
        
    else:
        return render(request,'login.html')
    
def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return redirect('insex')
    else:
        return redirect('/login')