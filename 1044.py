#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"

a, b = input().split(' ')
a = int(a)
b = int(b)

if(a % b == 0 or b % a == 0):
	print("Sao Multiplos")
else:
	print("Nao sao Multiplos")