a=4; b= 5 # Operator (=) assigns the value to variable
print(a, "is of type", type(a))
9/5
c = b/a # division returns a floating point number
print(c, "is of type", type(c))
c       # No need to explicitly delcare the datatype

a=4; b=5
d= b//a
print(d, "is of type", type(d))
7/5 # true division
-7//5 # floor division operator

a=7; b=5
e= b**a # The operator (**)calculates power
e
a%b

#Complex numbers

f=3+5j
print(f, "is of type", type(f))
f.real
f.imag
f*2 #multiplication
f+3 #addition
f-1 #subtraction

#Bool types

bool(2)
bool(-2)
bool(0)

See_boolean = (4*3 > 10) and (6+5 >= 11)
print(See_boolean)
if (See_boolean):
    print("Boolean expression returned True")
else:
    print("Boolean expression returned False")

#Representation error

1-0.9
1-0.9==.1
#Decimal module

import decimal
x=decimal.Decimal(3.14)
y=decimal.Decimal(2.74)
x*y
decimal.getcontext().prec=4
x*y

#Fraction module

import fractions
fractions.Fraction(3,4)
fractions.Fraction(0.5)
fractions.Fraction("0.25")

#Memebership, identiy, and logical operations

x=[1,2,3]
y=[1,2,3]
x==y #Test equivalence
x is y #Test object identiy
x=y #assignment
x is y

list() # an empty list
list1 = [1,2,3,4]
list1.append(1) #append value 1 at the end of the list
list1
