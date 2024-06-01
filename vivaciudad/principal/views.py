from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'principal/home.html')

def eventos(request):
    return render(request, 'principal/eventos.html')