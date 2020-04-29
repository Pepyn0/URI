#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"

a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)

if(a > b):
    maior = a
else:
    maior = b

if(maior < c):
    maior = c

print("%d eh o maior" %(maior))
