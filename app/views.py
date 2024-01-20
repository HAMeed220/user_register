from django.shortcuts import render

# Create your views here.

from app.forms import *

def Registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    
    d={'ufo':ufo,'pfo':pfo}

    return render(request,'Registration.html',d)