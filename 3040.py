#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"

def pode(N):
	saida = []
	for i in range(N):
		altura, diametro, galho = input().split(" ")
		altura = int(altura)
		diametro = int(diametro)
		galho = int(galho)

		if(condicao(altura, diametro, galho)):
			saida.append(1)
		else:
			saida.append(0)

	for i in saida:
		if(i == 1):
			print("Sim")
		else:
			print("Nao")

def condicao(altura, diametro, galho):
	if(altura < 200 or altura > 300):
		return False
	elif(diametro < 50):
		return False
	elif(galho < 150):
		return False
	else:
		return True



N = int(input())
pode(N)
