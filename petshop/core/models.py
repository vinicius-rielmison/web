from django.db import models

class Consulta(models.Model):

    nome_pet = models.CharField(max_length=100)
    idade_pet = models.CharField(max_length=20)
    especie = models.CharField(max_length=50)
    sexo = models.CharField(max_length=20)
    peso = models.CharField(max_length=20)
    raca = models.CharField(max_length=50)

    vacinas = models.CharField(max_length=200)
    doencas = models.CharField(max_length=200)
    medicamentos = models.CharField(max_length=200)
    cirurgias = models.CharField(max_length=200)
    alergias = models.CharField(max_length=200)

    atendimento = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)

    nome_dono = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_pet