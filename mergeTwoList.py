#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 09:20:26 2023

@author: anjulkumar
"""



def mergeTwoList(list1, list2):
    l1 = len(list1)
    l2 = len(list2)
    mergeList = []
    maxLength = 0
    if l1 == 0 and l2 == 0:
        return []
    elif l1 == 0:
        return list2
    elif l2 == 0:
        return list1
    elif l1 >= l2:
        maxLength = l1
    else:
        maxLength = l2
    c1 = 0
    c2 = 0
    while ((c1+c2) < (l1+l2)):
        if list1[c1] > list2[c2]:
            mergeList.append(list2[c2])
            c2 += 1
        elif list1[c1] < list2[c2]:
            mergeList.append(list1[c1])
            c1 += 1
        else:
            mergeList.append(list2[c2])
            mergeList.append(list1[c1])
            c1 += 1
            c2 += 1
    return mergeList


print(mergeTwoList([], [0]))