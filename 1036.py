#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"

import math

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

delta = (b**2) - (4 * a * c)

if(delta < 1 or a == 0):
	print("Impossivel calcular")
else:
	b = b * -1
	r1 = (b + math.sqrt(delta)) / (2 * a)
	r2 = (b - math.sqrt(delta)) / (2 * a)
	print("R1 = %.5f" %(r1))
	print("R2 = %.5f" %(r2))