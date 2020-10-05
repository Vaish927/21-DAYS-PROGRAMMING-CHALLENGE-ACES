# -*- coding: utf-8 -*-
"""

"""
#BUBBLE SORT ALGORITHM

n=int(input("Enter Size of array:"))

arr=list(map(int,input().split()))#input :integers separated by spaces

print("Unsorted Array:",arr)

for i in range(n):

    for j in range(n-i-1):

        if arr[j]>arr[j+1]:

            (arr[j],arr[j+1]) = (arr[j+1],arr[j])
            
print("Sorted Array:",arr)