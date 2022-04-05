#functions

from ast import arguments
from itertools import count
from turtle import st


def myFunction():
    print("This is my function")
    
def parameterFuntion(param):
    print(param)
    
def multiParamFunc(param1, param2):
    #this ony takes strings!!
    print(param1 + param2)
    
multiParamFunc("hello", "2")

def printSomeThings(*args):
    print("Order a pizza wiht these toppings")
    for arg in args:
        print(f" - {arg}".title())
        
printSomeThings(1, "something", "cheese", "pepperoni")

def pet(animal, name):
    print(f"I have a(n) {animal} named {name}.")

pet(name = "JOJO", animal = "cat")


def setAddress(street, city = "Fullerton", state = "CA", zip =  "92834", country = "USA"):
    print(street)
    print(city)
    print(state)
    print(zip)
    print(country)

setAddress("123, Elm St. ", zip = "92833")


x = lambda a :a*2
y = lambda a, b :a * b

print("********************")
print(x(10))

print(y(5,6))

def myLamb(n):
    "Pass in a num"
    return lambda a: a * n


#compares two nums and prints which ever larger
getMax = lambda a, b : a if a>b else b

myDoubler = myLamb(2)
myTripler = myLamb(3)
myQuadrupler = myLamb(4)
myQuintupler = myLamb(5)
print(myDoubler(11))
print(myTripler(11))
print(myQuadrupler(11))
print(myQuintupler(11))

