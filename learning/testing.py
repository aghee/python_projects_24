'''
i=1
while i<6:
    print(i)
    i+=1.1
'''
'''
numbers = [0, 254, 2, -1, 3]
for i in numbers:#i is the iteration variable,numbers is the iterable
    if i<0:#if condition not met,execute next level of indentation(print(i) in this case)
        print('Negative number found',i)
        break#escapes the loop, loop will not execute anymore
    print(i)
'''
'''
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
    if i<0:
        continue#do not execute any other code inside the loop,execute the next loop iteration
    print(i)#same level indentation as if,executes if 'if' condition is not met
'''
#while True:
    #pass
'''
n=99
sum=0
while True:
    sum+=n
    n-=1
    if n==0:
        break
print('The sum is:', sum)
'''
'''
#transposed matrix
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
for i in range(len(matrix[0])):
    transposed1=[]
    for k in matrix:
        transposed1.append(k[i])
    transposed.append(transposed1)
print(transposed)
#To revert to the original matrix
#variable transposed has 4 rows and 2 columns
#for i in range(2) executes first
#k[i] for k in transposed executes second
reverted1=[[k[i] for k in transposed] for i in range(2)]
print(reverted1)

single_digits=[0,1,2,3,4,5,6,7,8,9]
cubes=[i**3 for i in single_digits]
print(cubes)

#Sum of numbers in even positions in list
tsk=[0,1,2,3,4,5,6,7,8,9,10,11,12,19,21,42,88,80,99,78,32,33,47,45,33.4,32.2]
x=[]
y=[]
for index,item in enumerate(tsk,0):
    if index%2==0:
        x.append(item)
    if index%2 !=0:
        y.append(item)
print(x)
print(sum(x))
print(y)
print(sum(y))
'''
'''
#Simple recap of classes
class dogCat:
    att1='mamamlia'
    def __init__(self,breed,color,lifespan,ears):
        self.b=breed
        self.c=color
        self.lfpn=lifespan
        self.er=ears
        #print('self id is',id(self))
    def sleeps(self):
        print('This is a common trait in:',self.b)
        print(self.c,'are the best',self.b,'to keep in any household')
        print(self.b, 'has',self.er,'ears')
doggy=dogCat('gshepherd','blackish',9,2)
catty=dogCat('miawu','orange',99,4)
obj1=dogCat('Chihuahua','white',4.9,3)

print(doggy.b,'belongs to',doggy.__class__.att1,'species')
doggy.sleeps()
catty.sleeps()
obj1.sleeps()
#print(id(doggy))
'''
'''
#parent/base vs derived/child class
class parentOne:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        

    def display(self):
        print(self.name,self.id)

class childOne(parentOne):
    def __init__(self,name,id):
        super().__init__(name,id)
        #self.age=age
        #self.status=status
    def Printer(self):
        print('details are: ',self.name,self.id)

obj1=parentOne('parrot',20240)
obj1.display()
#print(id(obj1))
obj2=childOne('pride',1111)
obj2.Printer()
#obj2.display()
#print(id(obj2))
'''
'''
#Docstrings vs comments
def div(a,b):
    \'''Function that divides two numbers.\'''
    #if b==0:
        #raise ZeroDivisionError('Division by zero not allowed')
    return a/b
z=div(5,20)
print(z)

help(div)
print(div.__doc__)
print('#comment')
'''
'''
import math
def factorial(n):
    \'''Function showing factorial of number\'''
    if n == 0:  
        return 1
    else:
        return n *factorial(n - 1) 
       
print(factorial(4))
print(math.factorial(4- 1))
'''
#Closures - a function whose return value depends on the value of one or 
#more variable declared outside the function
#Closure function object remembers the value in the enclosing scope
#(thats is outer function) even if they are not present in the memory
'''
def func1(lst):
    \'''Enclosing scope.\'''
    def last_item(lst1):
        \'''Local scope.\'''
        return lst1[len(lst)-1]
    lst.remove(last_item(lst))
    return lst
lst=[1,8,9,3,4,7,2,22,99,6,5,35,89,85]
print(func1(lst))
print(func1(lst))
print(func1(lst))
'''
'''
def outer(sometext):
    def inner():
        \'''This is the Closure.\'''
        print(sometext)
    return inner #return inner function without parenthesis
a=outer('Hey you!')#a contains inner function
#delete outer function
del outer
#outer('Hey you') --outer is no longer defined but variable a remembers it
a()
#ADV OF CLOSURE -Used heavily in decorators
#1. Remembers value outside the scope
#2.Just like classes remember the state of variables and methods
#declared in the class,closures do so as well thus can be used 
#in place of classes that have fewer methods in them.
#3.Are sometimes more efficient than the normal functions-code efficiency

#print(id(func1(lst)))
#var1=func1(lst)
#print(id(var1))
'''
'''
def add(*args):
    add_num=0
    for i in args:
        add_num+=i
    return 'The sum of {} is {}'.format(args,add_num)
print(add(7,7,7,7,7,5))
'''
'''
lst=[5,4,3,2,1]
print(5*4*3*2*1)
print(lst[0]*sum(lst[1:]))
'''
#mutable vs immutable
'''
str1='mama'
print(id(str1))
str1='baba'
print(id(str1))

lista=[1,2,3,4,'maa','baa']
print(id(lista))
lista.append('zoom')
print(id(lista))
'''

lista=[1,4,5,8,9]
print(len(lista))

