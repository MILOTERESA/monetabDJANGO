from django.urls import path
from .views import index,modifier,ajouter

app_name='professeur'

urlpatterns = [
path('', index,name="professeur"),
path('ajouter_professeur/',ajouter,name='ajouter_professeur'),
path('modifier_professeur/',modifier, name='modifier_professeur'),

]

