from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),

    path('cadastro/', views.cadastro, name='cadastro'),

    path('horarios/', views.horarios, name='horarios'),

    path('consultas/', views.consultas, name='consultas'),

    # LOGIN PARA CLIENTE VER CONSULTAS
    path(
        'login-consultas/',
        views.login_consultas,
        name='login_consultas'
    ),

    # FUNCIONÁRIO
    path(
        'login-funcionario/',
        views.login_funcionario,
        name='login_funcionario'
    ),

    path(
        'painel-funcionario/',
        views.painel_funcionario,
        name='painel_funcionario'
    ),

    path(
        'funcionario-consultas/',
        views.funcionario_consultas,
        name='funcionario_consultas'
    ),

    path('deletar-consulta/<int:id>/', views.deletar_consulta, name='deletar_consulta'),

]