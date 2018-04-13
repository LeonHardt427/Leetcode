# -*- coding: utf-8 -*-
# @Time    : 2018/4/12 18:59
# @Author  : LeonHardt
# @File    : 0_quick_sort.py


#quick sort
def quickSort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[i]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1
        L[i] = L[j]+
        
        while i < j and L[i] <= key:
            i = i+1
        L[j] = L[i]
    L[i] = key
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L

if __name__ == '__main__':
    S = [3, 5, 4, 2, 6, 9, 1]
    e = quickSort(S, 0, 6)
    print(e)