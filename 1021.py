#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"




valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")

for nota in notas:
	quantidadeNota = int(valor / nota)
	print("%d nota(s) de R$ %.2f" %(quantidadeNota, nota))
	valor = valor - (quantidadeNota * nota)

print("MOEDAS:")
valor = valor * 100
for moeda in moedas:
	quantidadeMoeda = int(round(valor) / (moeda * 100))
	print("%d moeda(s) de R$ %.2f" %(quantidadeMoeda, moeda))
	valor = valor - (quantidadeMoeda * (moeda * 100))
