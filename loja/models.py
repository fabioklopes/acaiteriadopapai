from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class FormaPagamento(models.Model):
    class Meta:
        verbose_name = 'Forma de Pagamento'
        verbose_name_plural = 'Formas de Pagamento'
        ordering = 'forma_pagamento'

    forma_pagamento = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.forma_pagamento


class Mesa(models.Model):
    class Meta:
        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'
        ordering = 'mesa'

        # Mesa 001, Mesa 002, Mesa 003 ...
        numero_mesa = models.CharField(max_length=8, unique=True, null=False, blank=False)

        def __str__(self):
            return self.numero_mesa


class Produto(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = 'nome_produto'

        nome_produto = models.CharField(max_length=150, unique=True, null=False, blank=False)
        codigo_interno = models.CharField(max_length=65, unique=True, null=False, blank=False)
        peso = models.FloatField(null=False, blank=False)
        valor = models.FloatField(null=False, blank=False)
        margem_lucro = models.FloatField(null=False, blank=False)
        valor_venda = models.FloatField(null=False, blank=False)

        def __str__(self):
            return f"{self.codigo_interno} {self.nome_produto}"