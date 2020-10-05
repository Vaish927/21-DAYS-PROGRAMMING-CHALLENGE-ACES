# -*- coding: utf-8 -*-
"""

"""

#Insertion Sorting Algorithm

n=int(input("Enter Size Of Array:"))    
  
print("Enter Elements of Array:")

array=[int(input()) for i in range(n)]#using list comprehnsion

print("Unsorted Array:",array)

for i in range(1,len(array)):
    temp=array[i]
    j=i-1
    while(j>=0 and array[j]>temp):
         array[j+1]=array[j]
         j=j-1
         array[j+1]=temp
         
print("Sorted Array :",array)