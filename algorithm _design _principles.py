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
