#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"


tamanho = int(input())
masculino = 0
feminino = 0
for i in range(tamanho):
	frase, genero = input().split(" ")
	genero = str(genero)

	if(genero == 'M'):
		masculino += 1
	else:
		feminino += 1

print("%d carrinhos" %(masculino))
print("%d bonecas" %(feminino))