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
