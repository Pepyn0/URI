#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"



while True:
	tamanho = int(input())
	if(tamanho == 0):
		break
	i = 0
	contador = 0
	personagem = 1
	while(i < tamanho):
		D, M, E = input().split(' ')
		D = int(D)
		M = int(M)
		E = int(E)

		if(personagem == 1 and M == 1):

			if(D == 0):
				personagem = 0
				contador += 1

			elif(E == 0):
				personagem = 2
				contador += 1

		elif(personagem == 2 and E == 1):

			if(M == 0):
				personagem = 1
				contador += 1

			else:
				personagem = 0
				contador += 2

		elif(personagem == 0 and D == 1):

			if(M == 0):
				personagem = 1
				contador += 1

			else:
				personagem = 2
				contador += 2
					
		i += 1
	print(contador)