#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"

a, b, c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)

tri = a * c / 2
cir = (c ** 2) * 3.14159
tra = (a * c / 2) + (b * c / 2)
qua = b * b
ret = a * b

print("TRIANGULO: %.3f" %(tri))
print("CIRCULO: %.3f" %(cir))
print("TRAPEZIO: %.3f" %(tra))
print("QUADRADO: %.3f" %(qua))
print("RETANGULO: %.3f" %(ret))