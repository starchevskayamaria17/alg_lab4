#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insertion_sort(a):
    for i in range(len(a)):
        tmp = a[i]
        x = i - 1
        while x >= 0 and tmp < a[x]:
            a[x+1], a[x] = a[x], a[x+1]
            x -= 1
    return(a)
