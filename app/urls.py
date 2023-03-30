from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('saludo/',views.saludo,name='saludo'),
    path('index/<str:nombre>',views.index,name='index'),
    path('hincha/<int:num>',views.equipo,name='hincha'),
    
]