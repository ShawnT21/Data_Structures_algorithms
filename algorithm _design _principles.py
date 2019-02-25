def MatrixChain(mat, i, j):
 if i == j:
     return 0
minimum_computations = sys.maxsize
for k in range(i, j):
    count = (MatrixChain(mat, i, k) + MatrixChain(mat, k+1, j)+
mat[i-1] * mat[k] * mat[j])
    if count < minimum_computations:
           minimum_computations= count;
    return minimum_computations;

matrix_sizes = [20, 30, 45, 50];
print("Minimum multiplications are", MatrixChain(matrix_sizes , 1,
len(matrix_sizes)-1));

#Recursion

def factorial (n):
    # test for a base case
    if n ==0:
        return 1
        #make a calculation and a recursive call
    else:
        f = n*factorial(n-1)
        print(f)
        return(f)

factorial(4)

# Backtracking

def bitStr(n,s):
    if n==1: return s
    return [digit + bits for digit in bitStr(1,s) for bits in bitStr(n-1,s)]

print(bitStr(3,'abc'))

#Karatsuba algorithm
from math import log10
def karatsuba(x,y):

    #The base case for recusion
    if x<10 or y<10:
        return x*y

    #sets n, the number of digits in the highest input number
    n=max(int(log10(x)+1), int(log10(y)+1))

    #rounds up n/2
    n_2 = int(math.ceil(n/2.0))
    #adds 1 if n is uneven
    n = n if n%2 == 0 else n+1
    #splits the input numbers
    a, b = divmod(x, 10**n_2)
    c, d = divmod(y, 10**n_2)
    #applies the three recursive steps
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_bc = karatsuba((a+b), (c+d))-ac-bd

     #performs the multiplication
    return (((10**n)*ac)+bd+((10**n_2)*(ab_bc)))

t= karatsuba(1234,3456)
print(t)

#Merge Sort

def __mergeSort__ (A):
#Base case if the input is one or zero just return.
 if len(A) > 1:
    #splitting input array
    print('splitting', A)
    mid=len(A)//2
    left=A[:mid]
    right=A[mid:]
    #recursive calls to mergeSort for left and right subarrays
    mergeSort (left)
    mergeSort (right)
    #initalizes pointers for left (i) right (j) and output array (k)
    #3 initalization operations
    i = j = k = 0
    #Traverse and merges the sorted arrays
    while i < len(left) and j < len(right) :
    #if left < right comparasion operation
        if left[i] < right[j] :
        #if left < right assignment operation
            A[k] = left[i]
            i=i + 1
        else:
            #if right <= left assignment
            a[k] = right[j]
            j=j+1
            k=k+1
    while i< len(left):
    #assignment operation
        A[k] = left[i]
        i=i+1
        k=k+1
    while j< len(right):
    #assignment operation
        A[k] = right[j]
        j=j+1
        k=k+1
print('merging', A)
return(A)

mergeSort([356, 97, 846, 215])

import matplotlib.pyplot as plt
import math
x = list(range(1,100))
1 = []; 12 =[]; a=1
plt.plot(x, [y*y for y in x])
plt.plot(x, [7*y) *math.log (y,2) for y in x])
plt.show()
