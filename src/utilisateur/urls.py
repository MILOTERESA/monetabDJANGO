from django.urls import path
from .views import index,modifier,ajouter

app_name='utilisateur'

urlpatterns = [
path('', index, name = 'utilisateur'),
path('modifier_utilisateur',modifier, name ='modifier_utilisateur'),
path('ajouter_utilisateur' ,ajouter, name ='ajouter_utilisateur'),
]

