from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "professeur/professeur.html")
    
    
    
def modifier(request):
    return render(request,  "professeur/modifier_professeur.html")
    
    
def ajouter(request):
    
    return render(request, "professeur/ajouter_professeur.html")
    
    