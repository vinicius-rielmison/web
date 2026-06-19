from django.shortcuts import render, redirect, get_object_or_404
from .models import Consulta


def inicio(request):
    return render(request, 'inicio.html')


def cadastro(request):

    if request.method == "POST":

        nome_pet = request.POST['nomepet']
        idade_pet = request.POST['idadepet']
        cpf = request.POST['cpf']
        horario = request.POST['horario']

        if nome_pet == "":
            return render(request, 'cadastro.html', {"erro": "Nome do pet é obrigatório"})

        if not idade_pet.isdigit():
            return render(request, 'cadastro.html', {"erro": "Idade deve ser um número"})

        if len(cpf) != 11:
            return render(request, 'cadastro.html', {"erro": "CPF inválido"})

        if Consulta.objects.filter(horario=horario).exists():
            return render(request, 'cadastro.html', {"erro": "Esse horário já está ocupado"})

        consulta = Consulta(
            nome_pet=nome_pet,
            idade_pet=idade_pet,
            especie=request.POST['especie'],
            sexo=request.POST['sexo'],
            peso=request.POST['peso'],
            raca=request.POST['raca'],
            vacinas=request.POST['vacinas'],
            doencas=request.POST['doencas'],
            medicamentos=request.POST['medicamentos'],
            cirurgias=request.POST['cirurgias'],
            alergias=request.POST['alergiaspet'],
            atendimento=request.POST['atendimento'],
            horario=horario,
            nome_dono=request.POST['nomecliente'],
            cpf=cpf,
            telefone=request.POST['telefone'],
            email=request.POST['email'],
            endereco=request.POST['enderecocliente'],
        )

        consulta.save()

        return redirect('inicio')

    return render(request, 'cadastro.html')


def horarios(request):
    return render(request, 'horarios.html')


def consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consultas.html', {'consultas': consultas})


def login_funcionario(request):

    if request.method == "POST":

        email = request.POST['email']
        senha = request.POST['senha']

        if email == "admin@gmail.com" and senha == "mpe2026":
            return redirect('painel_funcionario')

        return render(request, 'login_funcionario.html', {'erro': 'Email ou senha inválidos'})

    return render(request, 'login_funcionario.html')


def painel_funcionario(request):
    return render(request, 'painel_funcionario.html')


def funcionario_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'funcionario_consultas.html', {'consultas': consultas})


def deletar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    consulta.delete()
    return redirect('funcionario_consultas')


def login_consultas(request):

    if request.method == "POST":

        email = request.POST['email']

        consultas = Consulta.objects.filter(email=email)

        if consultas.exists():
            return render(request, 'consultas.html', {'consultas': consultas})

        return render(request, 'login_consultas.html', {'erro': 'Email não encontrado'})

    return render(request, 'login_consultas.html')