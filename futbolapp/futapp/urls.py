from django.urls import path
from .views import (
    HomePageView, CustomLoginView, RegisterView, dashboard,
    equipos, profesores, jugadores, agregar_jugador, modificar_jugador, JugadorDeleteView, pagos,
    modificar_profesor, eliminar_profesor, agregar_profesor, agregar_pago, eliminar_pago, confirmar_eliminar_pago, modificar_pago
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/equipos/', equipos, name='equipos'),
    path('dashboard/profesores/', profesores, name='profesores'),
    path('dashboard/jugadores/', jugadores, name='jugadores'),
    path('dashboard/jugadores/agregar/', agregar_jugador, name='agregar_jugador'),
    path('dashboard/jugadores/modificar/<int:pk>/', modificar_jugador, name='modificar_jugador'),
    path('dashboard/jugadores/eliminar/<int:pk>/', JugadorDeleteView.as_view(), name='eliminar_jugador'),
    path('dashboard/profesores/', profesores, name='profesores'),
    path('dashboard/profesores/agregar/', agregar_profesor, name='agregar_profesor'),
    path('dashboard/profesores/modificar/<int:pk>/', modificar_profesor, name='modificar_profesor'),
    path('dashboard/profesores/eliminar/<int:pk>/', eliminar_profesor, name='eliminar_profesor'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('dashboard/pagos/', pagos, name='pagos'),
    path('dashboard/pagos/agregar/', agregar_pago, name='agregar_pago'),
    path('dashboard/pagos/modificar/<int:pk>/', modificar_pago, name='modificar_pago'),
    path('dashboard/pagos/confirmar_eliminar/<int:pk>/', confirmar_eliminar_pago, name='confirmar_eliminar_pago'),
    path('dashboard/pagos/eliminar/<int:pk>/', eliminar_pago, name='eliminar_pago'),
]


    
    