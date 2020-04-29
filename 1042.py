#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"



v = input().split(' ')
valor1 = []
valor2 = []
for i in v:
	valor1.append(int(i))
	valor2.append(int(i))

valor1.sort()

for i in valor1:
	print(i)
print()
for i in valor2:
	print(i)