#!/usr/bin/env python
# -*- coding: utf-8 -*-

def selection_sort(a):
    for i in range(len(a) - 1):
        tmp = i
        x = i + 1
        while x < len(a):
            if a[x] < a[tmp]:
                tmp = x
            x += 1
        a[i], a[tmp] = a[tmp], a[i]
    return a
