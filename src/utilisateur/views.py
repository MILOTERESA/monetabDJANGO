from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"utilisateur/utilisateur.html")

def ajouter(request):
    return render(request ,"utilisateur/ajouter_utilisateur.html")
    
def modifier(request):

    return render(request, "utilisateur/modifier_utilisateur.html")