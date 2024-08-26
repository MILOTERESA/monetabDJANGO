from django.urls import path
from .views import index,table

app_name='dashboard'


urlpatterns = [
path('', index, name = 'login'),
path('tableau_bord/',table, name = 'dashboard'),
]

