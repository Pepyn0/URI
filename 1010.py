#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"

a, b, c = input().split(' ')
d, e, f = input().split(' ')

b = int(b)
c = float(c)
e = int(e)
f = float(f)
f = f * e
c = c * b
f = f + c
print("VALOR A PAGAR: R$ %.2f" %(f))
