#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"


def eFinal(m):
	nota = float(input())

	print("Nota do exame: %.1f" %(nota))
	nota = (nota + m) / 2
	if(nota >= 5):
		print("Aluno aprovado.")
	else:
		print("Aluno reprovado.")
	print("Media final: %.1f" %(nota))



n1, n2, n3, n4 = input().split(' ')
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (2 * n1 + 3 * n2 + 4 * n3 + 1 * n4)
media = media / (2 + 3 + 4 + 1)

print("Media: %.1f" %(media))

if(media >= 7):
	print("Aluno aprovado.")

elif(media >= 5):
	print("Aluno em exame.")
	eFinal(media)
else:
	print("Aluno reprovado.")
