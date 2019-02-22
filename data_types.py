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
list2 = list1 *2
[1,2,3,4,1,1,2,3,4,1]
min(list1)

max(list1)

list1.insert(0,2) #insert an value 2 at index 0
list1

list1.reverse()
list1

list2=[11,12]
list1.extend(list2)
list1

sum(list1)

len(list1)

list1.sort()
list1
list1.remove(12) #remove value 12 from the list
list1

#Tuples

t = tuple() #create an empty tuple
type(t)
t=('a',) #create a tuple with 1 element
t
print('type is', type(t))
tpl=('a','b','c')
tpl=('a', 'b', 'c')
tuple('sequence')
x,y,z= tpl #multiple assignment
x
y
z
'a' in tpl #Memebership can be tested
'z' in tpl

tup1 = 1,2,3,4,5 #braces are optional
print("tuple value at index 1 is ", tup1[1])
print("tuple[1:3] is", tup1[1:3])
tup12 = (11, 12,13)
tup13= tup1 +tup12 #tuoke concatenation
tup13
tup1*2 #repetition for tuples
5 in tup1 #memebership test

tup1[-1]  #negative indexing

len(tup1) #length function for tuple

max(tup1)

min(tup1)

tup1[1] = 5 #modification in tuple is not allowed.

print(tup1 == tup12)
print(tup1>tup12)

1= ['one','two']
x,y = 1
x,y= y,x
x,y

#dictionaries

a = {'Monday':1, 'Tuesday':2, 'Wednesday':3} #creates a dictionary
b =dict({'Monday':1, 'Tuesday':2 , 'Wednesday':3})
b
c = dict(zip(['Monday', 'Tuesday', 'Wednesday'], [1,2,3]))
c={'Monday': 1, 'Tuesday': 2, 'Wednesday': 3}
d= dict([('Monday',1), ('Tuesday',2), ('Wednesday',3)])
d

d['Thursday'] =4 #add an item
d.update({'Friday':5, 'Saturday':6}) #add multiple items
d
'Wednesday' in d #Memebership test (only keys)
5 in d #Memebership do not check in values

dict(zip('packt', range(5)))
{'p': 0, 'a': 1, 'c': 2, 'k': 3, 't': 4}
a = dict(zip('packt', range(5)))
len(a) #length of dictionary a

a['c'] # to check the value of a key

a.pop('a')

a{'p':0, 'c': 2, 'k': 3, 't': 4}
b= a.copy() #make a copy of the dictionary
b
a.keys()
a.values()
a.items()
a.update({'a':1}) # add an item in the dictionary
a{'p': 0, 'c': 2, 'k': 3, 't': 4, 'a': 1}
a.update(a=22) #update the value of key 'a'
a{'p': 0, 'c': 2, 'k': 3, 't': 4, 'a': 22}

#Sorting dictionaries
d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
sorted(list(d))

sorted(list(d.values()))

sorted(list(d), key = d.__getitem__)

[value for (key, value) in sorted(d.items())]

sorted(list(d), key = d.__getitem__ , reverse=True)

d2= {'one': 'uno', 'two':'deux', 'three': 'trois', 'four': 'quatre', 'five':'cinq',
'six':'six'}

sorted(d2, key=d.__getitem__)

[d2[i] for i in sorted(d2, key=d.__getitem__)]
def corder(string):
    return (string[len(string)-1])
    sorted(d2.values(), key=corder)
    ['quatre', 'uno', 'cinq', 'trois', 'deux', 'six']

#dictionaries for text analysis

def wordcount(fname):
    try:
        fhand=open(fname)
    except:
        print('File can not be opened')


#Deques

dq2=deque([], maxlen=3)
for i in range(6):
    dq2.append(i)
    print(dq2)


import collections
dict1={'a':1, 'b':2,'c':3}
dict2={'d':4, 'e':5}
chainmap=collections.ChainMap(dict1, dict2)
chainmap
ChainMap ({'a':1,'b':2,'c':3},{'d':4,'e':5})
chainmap.values
<bound method Mapping.values of ChainMap({'a':1,'b':2,'c':3},{'d':4, 'e':5})
chainmap['b']
chainmap['e']

from collections import ChainMap
defaults={'theme':'Default','language':'eng','showIndex':True,}
'showFooter':True}
cm= ChainMap(defaults) #creates a chainMap with defaults configuration
cm.maps[{'theme': 'Default', 'language': 'eng','showIndex':True,
'showFooter':True}]
cm.values()
ValuesView(ChainMap({'theme': 'Default', 'language':'eng', 'showIndex':True, 'showFooter': True}))
cm2= cm.new_child({'theme':'bluesky'}) #create a new ChainMap with a child that overrides the parent.
cm2['theme'] #returns the overrides theme 'bluesky'
cm2.pop('theme') #removes the child theme value 'bluesky'
cm2['theme']
'default'
cm2.maps[{}, 'theme':'Default', 'language': 'eng','showIndex':True,'showFooter':True]
cm2.parents
ChainMap({'theme':'Default', 'language': 'eng', 'showIndex': True, 'showFooter':True})


# Counter object

from collections import Counter
Counter('anysequence')
Counter({'e': 3, 'n': 2, 'a': 1, 'y':1, 's': 1, 'q': 1, 'u': 1, 'c': 1})
c1 = Counter('amysequence')
c2 = Counter({'a': 1, 'c': 1, 'e': 3})
c3 = Counter(a=1, c= 1, e=3)
c1
Counter({'e': 3, 'n': 2, 'a': 1, 'y': 1, 's': 1, 'q': 1, 'u': 1, 'c': 1})
c2
Counter({'e': 3, 'a': 1, 'c': 1})
c3
Counter({'e':3, 'a': 1, 'c': 1})

#Another way to Counter
ct
Counter({'a':5, 'b': 1, 'c':1})
ct['x']
ct.update({'a': -3, 'b':-2, 'e';2})
ct
Counter({'a': 2, 'e': 2, 'c': 1, 'b': -1})
sorted(ct.element())
ct.most_common()
[('a',2), ('e', 2), ('c', 1), ('b', -1)]
ct.substract({'e':2})
ct
Counter({'a':2, 'c':1, 'e': 0, 'b': -1})

#OrderdDict
import collections
od3 = collections.OrderedDict(sorted(od1.items(), key= lambda t:(4*t[1])-t[1]**2))
od3
