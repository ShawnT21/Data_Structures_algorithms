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
