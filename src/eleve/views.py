from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,"eleve/eleve.html")
    
def modifier_eleve (request):
    return render(request,"eleve/modifier_eleve.html")
    
def ajouter_eleve (request):
    
    
    return render(request,"eleve/ajouter_eleve.html")
    
