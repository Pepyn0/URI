#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"

valor = float(input())
if(valor >= 0 and valor <= 25.0000):
    print("Intervalo [0,25]");
elif(valor > 25.0000 and valor <= 50.00000):
    print("Intervalo (25,50]");
elif(valor > 50.00000 and valor <= 75.00000):
    print("Intervalo (50,75]");
elif(valor > 75.00000 and valor <= 100):
    print("Intervalo (75,100]");
else:
    print("Fora de intervalo");
