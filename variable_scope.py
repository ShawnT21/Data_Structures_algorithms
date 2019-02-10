a = 15;b=25
def my_function ():
   global a
   a=11;b=21

my_function()
print(a)
print(b)

a = 10
def my_function():
    print(a)
my_function ()

#How to fix outofbound error
#make a global
a = 10
def my_function():
    global a
    print(a)
    a= a +1
my_function()

#Flow control and iteration

x='one'
if x==0:
    print('False')
elif x ==1:
     print('True')
else:    print('Something else')

words = ['cat', 'dog', 'elephant']
for w in words:
      print(w)


  if a==b: # a and b have the same vaule

  if a is b: #If a and b are the same object

   if type(a) is type(b) #a and b are the same type

greet = "hello world"
for i in enumerate(greet[0:5]):
    print(i)
greet[:5] + ' wonderful' + greet[5:]

x='3'; y='2'
x + y #concatenation

int(x) + int(y) #addition

#Lists

x=1;y=2;z=3

list1 =[x,y,z]
list2 = list1
list2[1] = 4
list1

items = [["rice",2.4, 8], ["flour", 1.9, 5], ["Corn", 4.7, 6] ]
items[1][1]= items[1][1]*1.2
for item in items:
    print("Product: %s Price: %.2f Qaulity: %i" % (item[0], item[1], item[2]))

#List comprehensions

l= [2,4,8,16]
[i**3 for i in l]

def f1(x): return x*2
def f2(x): return x*4

lst =[]
for i in range(16):
    lst.append(f1(f2(i)))
print(lst)
print([f1 (x) for x in range(64) if x in [f2(j) for j in range(16)]])

list1= [[1,2,3], [4,5,6]]
[i*j for i in list1[0] for j in list1[1]]

words = 'here is a sentence'.split()

[[word, len(word)] for word in words]


#Functions as first Class objects
def greeting(language):
    if language=='eng':
        return 'hello word'
        if language =='fr':
         return 'bonjour le monde'
    else: return 'language not supported'

l=[greeting('eng'), greeting('fr'), greeting('ger')]
l[1]
 def callf(f):
     lang='eng'
     return(f(lang))

callf(greeting)

#Higher order Functions

list = [1,2,3,4]
for item in map(lambda n: n*2, list): print(item)

list = [1,2,3,4]
for item in filter(lambda n: n<4, list): print(item)

words=str.split('The longest word in this sentence')
sorted(words, key=len)

sl=['A','b','a','C','c']
sl.sort(key=str.lower)
sl
sl.sort()
sl

items=[['rice',2.4,8],["flour",1.9,5],["Corn", 4.7,6]]
items.sort(key=lambda item: item[1])
print(items)




#Recursive Functions
def iterTest(low,high):
    while low <= high:
        print(low)
        low=low+1

def recurTest(low,high):
    if low <= high:
        print(low)
        recursTest(low+1, high)

#Generators and co-routines

#Compares the running time of a list compared to a Generator
import time
#generator function creates an iterator of odd numbers between n and m
def oddGen(n,m):
    while n<m:
      yield n
      n+=2
#Builds a list of odd numbers between n and m
def oddLst(n,m):
    lst=[]
    while n<m:
        lst.append(n)
        n+=2
    return lst
#the time it takes to perform sum on an iterator
t1=time.time()
sum(oddGen(1,1000000))
print("Time to sum an iterator: %f" % (time.time() - t1))
#the time it takes to build and sum a list
t1=time.time()
sum(oddLst(1,1000000))
print("Time to build and sum a list: %f" % (time.time() - t1))

lst1 =[1,2,3,4]
gen1 = (10**i for i in lst1)
gen1
for x in gen1: print(x)
