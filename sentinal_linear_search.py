# -*- coding: utf-8 -*-
"""

"""  
  
# Function to search x in the given array  
n=int(input("Enter Size of Array:"))
print("Enter Elements in Array")
arr=[int(input())for i in range(n)]
print(arr)
x=int(input("Enter Search Element:"))
def sentinelSearch(arr, n, x) :  
  
    # Last element of the array  
    last = arr[n - 1] ; 
  
    # Element to be searched is  
    # placed at the last index  
    arr[n - 1] = x ; 
    i = 0;
  
    while (arr[i] != x) :  
        i += 1;
  
    # Put the last element back  
    arr[n - 1] = last  ;
  
    if ((i < n - 1) or (x == arr[n - 1])) :  
        print(x, "is present at index", i)  ;
    else : 
        print("Not found") ; 
  
# Driver code  

  
sentinelSearch(arr, n, x) ;