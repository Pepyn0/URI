#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"


N = int(input())
i = 0
while(i < N):

	string = input()
	tamanho = len(string)
	lista = list(string)

	for j in range(tamanho):
		if(lista[j] >= 'a' and lista[j] <= 'z'):
			lista[j] = chr(ord(lista[j]) + 3)

		if(lista[j] >= 'A' and lista[j] <= 'Z'):
			lista[j] = chr(ord(lista[j]) + 3)

	for k in range(int(tamanho / 2)):
		aux = lista[k]
		lista[k] = lista[tamanho - 1 - k]
		lista[tamanho - 1- k] = aux

	for k in range(int(tamanho / 2), tamanho, +1):
		lista[k] = chr(ord(lista[k]) - 1)

	string = ''.join(lista)
	print(string)
	i += 1