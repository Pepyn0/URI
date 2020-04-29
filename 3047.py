#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"

M = int(input())
A = int(input())
B = int(input())

C = M - A - B

if(C > A and C > B):
	print(C)
elif(A > B and A > C):
	print(A)
else:
	print(B)