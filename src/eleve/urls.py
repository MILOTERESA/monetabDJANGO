from django.urls import path
from .views import index, ajouter_eleve, modifier_eleve

app_name='eleve'

urlpatterns = [
path('', index, name = 'eleve'),
path('ajouter_eleve', ajouter_eleve, name = 'ajouter_eleve'),
path('modifier_eleve', modifier_eleve, name = 'modifier_eleve'),
]

