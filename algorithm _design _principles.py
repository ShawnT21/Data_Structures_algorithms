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
