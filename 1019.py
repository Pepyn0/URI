#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__		= "Pepyn0"
__copyright__	= "Copyright 2020, eXu Corp.dev"

HS = 3600

T = int(input())
H = int(T / HS)

M = int((T - (HS * H)) / 60)
S = int((T - (HS * H) - (M * 60)))

print("%d:%d:%d" %(H,M,S))
