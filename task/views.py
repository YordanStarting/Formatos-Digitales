from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    title = 'BIENVENIDO AL IMALAYA'
    return render(request, 'index.html', {'titulo': title})

def login(request):
  
    return render(request, 'login.html', {'form': UserCreationForm})
