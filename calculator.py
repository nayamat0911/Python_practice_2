"""
print(2+4*4-3)
print(6/3)
print(6//3)
print(5/3)
print(5//3)
"""
#new lesseon
"""
print("Today's lessone")
for i in range(2,30,2):
    print(i)

print("loop")
for i in range(1,10,4):
    print(i)

print("range")
for i in range(1,5,2):
    print(i)
"""
""" print("infinit loop")
while True:
    print("please enter name:")
    name=input()
    if name == "you name":
        break
print("thank you")

print("again")

while True:
    print("Who are you?")
    name = input()
    if name != 'akash':
        continue
    print("hello"+ name +"what is your pass code?")
    passcode = input()
    if passcode == "1234":
        break

print("enter akash")
"""
"""
while True:
    print("who are you?")
    name = input()
    if name != 'kamal':
        continue
    print("Hi "+ name + " how are you?")
    password = input()
    if password == "fine":
        break

print("thank you " + name)
"""
"""
print("loop")
sum = 0
for i in range(1,10,1):
    print(sum)
    sum = sum + i * i

print(sum)



def f():
    print("hello")

f()

def sum(a,b):
    return a+b

a = sum(1,2)
print(a)

def print_my_name(name):
    print('my name is  '+ name)

my_name =input()
print_my_name(my_name)

var = print("ok")
print(type(var))
print("hello ",end='')
print("world")
print('a', 'b', 'c', 'd', sep='-')

def f():
    c =10
    print(c)
f()
#
# print(c)

"""
"""
def func():
    global a
    print(a+2)
a=19
func()
"""
'''
def pop():
    print(x)
    x =100
x=100
print(x)
'''
#p
# rint("skw",'name', 'kamal', 5,6, sep=',')

a="I"
b = "love"
c= "you"
print("hey", a,b,c)

print("%s love %s"%(a,b))

n0name="anis"
print(n0name)

a=5
b = 5.4
c ="name"
d= (1,2,3,4)
e={1,2,3,4,5}
f=[1,2,3,4,5,6,7]
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(a,b,c,d,e,f, sep="\n")
x,y,z,h="hasan", "kamal", "manik","jalam"
print(c+ " "+ h)
print(x,y,z,h, sep="\n")
x=y=z="nayamt"
print(x,y,z)
del z
print(x,y)
# a = input("plz enter name: ")
# b =int(input())
# c = float(input())
# print(type(a))
# print(type(b))
# print(type(c))
# a,b,c,d = input("enter your number :").split("*")
# print("{} {} {} {}".format(a,b,c,d))

import keyword
print(keyword.kwlist)

#1 arithmetic operators
#2 Assignment Operatos
#3 Comparison Operatos
#4 Logical Operatos
#5 Identify Operators
#6 Membership Operators
#7 Bitwise Operators
#8 Tenary perators
print("Arethmetic operatos= add, sub, mul,div,mod, power")
print("arethmetic perators")
print(10+5)
print(10-5)
print(10*5)
print(10/5)
print(5//3)
print(10%3)
print(20**3)

print("Comparisom Operators= Equal==, Not equal !=, Greter than >, less than <, Greter than or Equal to >= , less than or equal to <=  ", sep="\n")
a=20
b=4
print(a==b)
print(a !=b)
print(a>b)
print(a<b)
print(a >= b)
print(a<=b)

