#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"

def perimetroTriangulo(a, b, c):
	print("Perimetro = %.1f" %(a + b + c))

def areaTrapezio(a, b, c):
	aux = (a + b) * c / 2
	print("Area = %.1f" %(aux))


a, b, c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)

if((a + b) > c and (a + c) > b and (b + c) > a):
	perimetroTriangulo(a, b, c)
else:
	areaTrapezio(a, b, c)