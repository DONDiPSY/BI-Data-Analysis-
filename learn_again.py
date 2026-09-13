# checking version on IDE

# A multi line comment

"""
import sys

print(sys.version)

if 5 > 2:
    print('This is true')

# variable are containers for storing data values
x = 5
y = "Hello Word!"
print(x)
print(y)

#  python casting
x = str(3)
print(x)

# data type
print(type(x))

mvar_ = 'Hello'
print(mvar_)

# assign multiple values to a multiple variable
x, y, z = 4, 5, 6
print(x)
print(y)
print(z)

# assign one values to a multiple variable
x = y = z = 4
print(x)
print(y)
print(z)

# Extracting values into a variable
fruits = ['apple', 'banana', 'cherry']
x, y, z = fruits
print(x)
print(y)
print(z)

# output variable
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# creating and using a Global variable
x = 'awesome'


def myfunc():
    print('python is ' + x)


myfunc()

# creating a variable inside a function
# with the same variable name is called local variable
x = 'awesome'


def myfunc():
    x = 'fantastic'
    print('python is ' + x)


myfunc()
print('python is ' + x)

# global keyword

x = 'fantastic'


def myfunc():
    global x
    x = 'Beautiful'
    print('life  is ' + x)


myfunc()

z = range(7)
print(z)

# Numeric data types
f = -87.7e100
print(f)

# looping Through a string
for x in "banana":
    print(x)

# String Length
x = "banana"
print(len(x))

# check String
txt = "The best things in life are free!"
print("free" in txt)

# use it in an if statement
txt = "The best things in life are free!"
if "free" in txt:
    print("Life is Beautiful")

# check if not
txt = "The best things in life are free!"
print("free" not in txt)

txt = "The best things in life are free!"
if "free" not in txt:
    print("Love")
else:
    print('passion for coding')

# slicing string
a = 'Hello, World!'
print(a[3:8])

# Modify String
a = " Life is crazy "
print(a.upper())
print(a.lower())
print(a.replace("Life", "Football"))
print(a.split(","))
print(a.strip())


# Format String with a function and modifies


def myfunc(name, age):
    return f'My name is {name} and my {age:.4f}'


print(myfunc("James", 24))

# it is use check datatype of a boolean
x = 50
print(isinstance(x, int))

# print a message based on whether the condition is true
# False in return
r = "Glad I'm doing this"
j = "So happy "
if 4 < len(r):
    print("God is marvellous")
else:
    print("Oops!")


def myfunc():
    return True


if myfunc():
    print('Yes')
else:
    print('No')

x = 5
print(x > 2)

# Augment assignment operator
x = 10
x += 3
print(x)

# input
x = input("x: ")
y = int(x) + 1
print(f'x: {x}, y: {y}')

# ternary operator
#  choosing values based on conditions.
age = 30
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

love = 40
life = " flowers are Beautiful" if love <= 20 else "you so ugly"
print(life)

if (length := len("hello world")) > 5:
    print(f"String is long: {length}")

# logical

# loop
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Level is successful")
        break
else:
    print("level Terminated")

# XOR

a = 10
b = 5
a ^= b
b ^= a
print(a)
print(b)

x = 10
y = 5
z = x | y
print(z)

numbers = [2, 3, 2, 4]
unique_no = 0
for num in numbers:
    unique_no ^= num

print(unique_no)

# walrus
while (line := input("Enter a line or exit: ")) != "exit":
    print(f"you have entered : {line}")

data = [2, 4, 5, 3]
squared = [square for x in data if (square := x ** 2) > 5]
print(squared)

mylist = ["apple", "cherry", "mango"]
mylist[1:2] = ["blackcurrant", "orange"]
print(mylist)

this_list = ['apple', 'banana', 'cherry']
this_tuple = {"kiwi", "orange"}
this_list.extend(this_tuple)
print(this_list)

this_list = ['apple', 'banana', 'cherry']
new_list = []

for x in this_list:
    if 'a' in x:
        new_list.append(x)

print(new_list)
NewList = new_list.count('apple')
print(NewList)
this_list.insert(2, "mango")
print(this_list)

del this_list[0]

fruits = ['apple', 'banana', 'cherry', 'mango', 'kiwi']
new_list = [x for x in fruits if 'a' in x]
print(new_list)
i = 0
while i > len(fruits):
    print(fruits[i])
    i += 1


def myfunc(n):
    return abs(n - 50)


mylist = [100, 30, 40, 60, 120]

mylist.sort(key=myfunc)
print(mylist)

people = [
    {"Name": "Bam", "Age": 25},
    {"Name": "James", "Age": 40},
    {"Name": "Philip", "Age": 27}
]


def customize_sort(person):
    return person['Age'], person['Name']


sorted_people = sorted(people, key=customize_sort)

for person in sorted_people:
    print(f"Name:{person['Name']} - Age:{person['Age']}")

books = ('habit', 'sharp', 'king', 'queen')

sort_book = sorted(books)
print(sort_book)

your_list = ['cat', 'dog', 'goat', 'sheep']
your_list[0:2] = ['bird', 'snake', 'mouse']
print(your_list)

while (line := input('Enter a line or exit: ')) != "exit":
    print(f"your entered: {line}")

line = input('Enter a line or exit: ')

while line != 'exit':
    print(f"your entered: {line}")
    line = input('Enter a line or exit: ')

my_tuple = ('love',)
print(type(my_tuple))

set1 = {'Google', 'Microsoft', 'Oracle', 'Apple'}
if 'Google' in set1:
    for x in set1:
        print(x)

set1.add('BIS')
print(set1)

n = 20
f = 30
if (n := 10) and (f := 20):
    print(f"n : {n} , f : {f}")

data = [1, 5, 6, 8, 9]
multi = [mx for x in data if (mx := x * 5) > 5]
muti = []
for x in data:
    if x > 5:
        y = x * 2
        muti.append(y)
print(muti)

while (line := input("Enter your line or Enter exit to quit: ")) != "exit":
    print(f"Your Enter a line : {line}")

line = input("Enter your line or Enter exit to quit: ")

while line != "exit":
    line = input("Enter your line or Enter exit to quit: ")
    print(f"Your Enter a line : {line}")

full = "Love your neighbour"

a = full.split(' ')
print(a)
print(' -  '.join(a))

mylist = ["ball", "cat", "john"]
if "ball" in mylist:
    print("Yes present")
# x = mylist.pop(1)
# del mylist[1]
for i in range(len(mylist)):
    print(mylist[i])

numbers = [1, 2, 3, 4, 5, 6]
even_number = []
for num in numbers:
    if num % 2 == 0:
        even_number.append(num)
print(even_number)

new_list = ['apple', 'banana', 'cherry', 'mango', 'kiwi']
pap_list = []
for x in new_list:
    y = x.upper()
    pap_list.append(y)
print(pap_list)

who_list = [print(x.upper()) for x in new_list]

pall_list = [x if x != 'banana' else 'orange' for x in new_list]

Employee = [
    {'Name': 'Peter', 'Department': 'Accountant'},
    {'Name': 'Moses', 'Department': 'Engineer'},
    {'Name': 'David', 'Department': 'Sale Representative'}
]


def company(arrange):
    return arrange['Name'], arrange['Department']


sort_employee = sorted(Employee, key=company)

for arrange in sort_employee:
    print(f"* {arrange['Department']} \n Name : {arrange['Name']}")


def win(n):
    return abs(n - 20)


your_list = [90, 20, 30, 40, 90, 100]

your_list.sort(key=win)

print(your_list)
z = your_list
k = z.copy()
print(k)

set1 = {4, 6, 7, 8}
set2 = [4, 6, 7, 8]
t = set1.isdisjoint(set2)
print(t)

my_tub = (1, 2, 3, [10, 20, 30], 'Hello')
my_tub[3].append(60)
print(my_tub)

Valid = {(1, 2), (3, 4), (6, 8)}
# list constructor
myvalid = list(Valid)
print(myvalid)

#iterate the tuple in the list to a list constructor
# using the range along with index
start, end = 0, 2
for i in range(start, end + 1):
    myvalid[i] = list(myvalid[i])

print(myvalid)

#print(x_valid[start:end])

car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1965
}
x = car.items()
print(x)
print("Update items")
car["color"] = 'Red'
print(x)

motors = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
if "model" in motors:
    print(f"yes ,{motors['model']} is one of the key in motors")

Vegas = ['apple', 'banana', 'cherry', 'mango', 'kiwi']
Fruits = []
for x in Vegas:
    if x != 'banana':
        Fruits.append("orange")
    else:
        Fruits.append(x)

print(Fruits)


new_list = [x if x != "banana" else 'orange' for x in fruits]
motors = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946
}
motors.pop("model")
print(motors)

for x in motors:
    print(x)
for x in motors:
    print(motors[x])
for x, y in motors.items():
    print(x, " : ",  y)





family = {
    'child1': {
        'name': 'Dave',
        'year': 1945
    },
    'child2': {
        'name': 'John',
        'year': 1925
    },
    'child3': {
        'name': 'Paul',
        'year': 1965
    },
    'child4': {
        'name': 'Tomi',
        'year': 2002
    }
}
print(f"Name: {family['child4']['name']},  \nDate of Birth: {family['child4']['year']}.")

for x, y in family.items():
    print(x)
    for z in y:
        print(z + " : ", y[z])
my_dict = {'a': 1, 'b': 2, 'c': 3}
result = my_dict.setdefault('j', 10)
print(result)
print(my_dict)

# Extend a list in a dict, using setdefault method
w = {"fruits": ['apple', 'cherry', 'mango']}
z = w.setdefault('fruits', []).append('pineapple')
print(w)
k = {"fruits": ['apple', 'cherry', 'mango']}
r = k.setdefault('vegetable', []).extend(['Tomatoes', 'onions', 'Bell-pepper'])
print(k)
k['Spice'] = []
k["Spice"].extend(['Curry', 'Maggi', 'Time'])
print(k)
family.update({"child5": {"name": "Adedolapo", "Age": [13, 14, 15], 'Occupation': "BI Analyst"}})
family["child5"]["Age"][1] = 29
print(family)

x = 42
if x > 10:
    print("Above ten")
    if x > 20:
        print("and also above 20!")
else:
    print("but not above 20")

i = 0
while i <= 10:
    print(i)
    if i == 6:
        break
    i += 3

print("continue")


fruits = ["orange", "apple", "mango", "cherry"]
for x in fruits:
    print(x)
    if x == "mango":
        break

fruits = ["date", "grapes", "cherry"]
for x in fruits:
    if x == "grapes":
        continue
    print(x)


def com(n):
    return abs(n - 100)


my_list = [50, 40, 60, 70, 80]
my_list.sort(key=com)
print(my_list)


def my_fun(lname):
    print(f"My name is {lname}")


my_fun("Ayodeji")


def my_functions(*kids):
    print(f"The youngest child is {kids[2]}")


my_functions("mike", "john", "jamal", "favour")


def my_functions(family):
    print(f"The oldest child is {family['child5']['name']}. \nHe is an aspiring {family['child5']['Occupation']}.")


my_functions(family)


def my_function(child3, child2, child1):
    print(f"The oldest child is {child1}")
    print(f"The second born is {child2}")
    print(f"The youngest is {child3}")


my_function(child1="peter", child2="tobias", child3="love")


def your_fun(**Books):
    print(f"My first read when it comes to motivational book was {Books['name']}")
    print(f"I would love to read {Books['fname']}")


your_fun(name="Atomic Habit", fname=" The 7 Habit of Highly Effective People")

# using a  customize function with a loop and  sort print  the list by sorting
# while using function with a loop will iterate the list
skin_care = ["Perfumes", "Sun screen", "Body lotion", "Roll on"]


def my_func(beauty):
    for x in range(len(beauty)):
        return beauty[x]


skin_care.sort(key=my_func)
print(skin_care)


# my_func(skin_care)

def your_fun(pretty):
    for x in range(len(pretty)):
        print(pretty[x])


your_fun(skin_care)


def you_can(lover, *, yo):
    print(f"My lover have a big {lover}, I can't wait to {yo}")


you_can('ass', yo="fuck")


# recursion



# writing alphabet  A - z


child1 = {'name': 'Adedolapo', 'Age': 50}
child2 = {'name': 'Tomilola', 'Age': 44}
child3 = {'name': 'Temitope', 'Age': 48}
family4 = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(family4["child1"])
for x in family4.values():
    print(f"My name is {x['name']} , i'm {x['Age']} of age")

Yummy = {'food': ['Pounded Yam'], 'Method': ['cook', 'pound']}
Yummy.setdefault('food', ['Pounded Yam']).extend(['Rice', 'Garri'])
print(Yummy)

i = 1
while i <= 10:
    i += 3
    if i == 7:
        continue
    print(i)

i = 1
while i <= 10:
    print(i)
    if i == 7:
        break
    i += 3

fruits = ["date", "grapes", "cherry"]
for x in fruits:
    print(x)
    if x == "grapes":
        break


# Arbitrary Arguments: *args


def playtime(*play):
    print(f"i love {play[1]}, and  {play[2]}")


playtime('football', 'boxing', 'basketball')


# keyword Arguments


def baller(first, third):
    print("my first love was " + first)
    print("she was just so " + third)


baller(first="Joyce", third="pretty")


# Arbitrary keyword Arguments **arg
def caller(joy='beautiful', **pain, ):
    print(f"what kind {pain['little']} are you feeling? \nYes i enjoy the {pain['calm']},just so {joy}")


caller(little='relief', calm='rest ')


# recursion
def myfun(n):
    if n > 0:
        result = n + myfun(n - 1)
        print(result)
    else:
        result = 0
    return result


myfun(6)


def myfun(char):
    if char > 'Z':
        return "Z"

    else:
        print(char, end=" ")
        myfun(chr(ord(char) + 1))


myfun('A')


def factorial(f):
    if f == 0 or f == 1:
        return 1
    else:
        return f * factorial(f - 1)


print("\n", factorial(5))


def my_dun(alphabet):
    if alphabet < "A":
        return "A"
    else:
        print(alphabet, end=" ")
        my_dun(chr(ord(alphabet) - 1))


my_dun("Z")


def fun_time(fib):
    if fib == 0:
        return 0
    elif fib == 1:
        return 1
    else:
        fib_m = fun_time(fib - 1) + fun_time(fib - 2)
        print(f"\nfib({fib})= fib({fib - 1}) + fib({fib - 2}) = {fib_m}")
        return fib_m


fun_time(6)

thisdict = {
    "brand": "ford",
    "model": "Mustang",
    "year": 1946,
    "year": 2020
}
print(thisdict)
thisdict.update({"colors": ['red', 'blue', 'green']})
print(thisdict)
x = thisdict.get("colors")
print(x)
thisdict['model'] = "SRT"
print(thisdict)

a = 500
b = 400
c = 200
if a < b or c > a:
    pass
else:
    print("Oops!")

w = [43, 20, 30]
if 70 in w:
    print("Hurray!")
    if 50 in w:
        print("Lol")
    else:
        print("Yummy!")
else:
    print("chai!")

w = [40, 17, 30,50, 20, 12, 13]
x = sorted(w, key=lambda p: p * 5 )
print(tuple(x))

import math

w = [25, 15, 30, 144, 100, 121, 400]
x = filter(lambda p: math.sqrt(p) % 2 == 0, w)
print(tuple(x))


class Young:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I name is {self.name}, {self.age}"

    def pof(self):
        print(f"I'm {self.age} years old")


yg = Young("Paul", 36)
print(yg)
yg.pof()


class Myclass:
    j = "to code"
    k = "Relearn"

    @staticmethod
    def prof(n="week"):
        print(f"I'm happy to start code this {n}")

    @classmethod
    def pull(cls):
        print(f"What a wonderful day {cls.j}, and {cls.k}")


Myclass.prof()
Myclass.pull()
# print out an object_method by accessing a dictionary
Gender = {
    "Name": "Adedolapo",
    "Age": 29,
    "color": ["black", "white", "red"],
    "Favourite_car": "Mustang",
    "favourite_snacks": "Meat_pie",
    "Year": 1996
}


class wip:
    def __init__(self, Gender):
        self.Gender = Gender

    def pull(self):
        print(f"I'm {self.Gender['Name']} by name ,\nMy favourite snacks{self.Gender['favourite_snacks']}")


sweep = wip(Gender)
sweep.pull()


# python Inheritance


class loop:
    def __init__(self, top, shop):
        self.top = top
        self.shop = shop

    def zoop(self):
        print(self.top + " Moving to the", self.shop)


class keep(loop):
    def __init__(self, top, shop, drop):
        super().__init__(top, shop)
        self.drop = drop

    def long(self):
        print(f"{self.drop} {self.top}  {self.shop}")


shoop = loop("We are", "Top")
shoop.zoop()
zip = keep("Task on practise", "will make", "you an expert")
zip.long()


# iterator

# myit = iter(mylist)
# print(next(myit))
# print(next(myit))
# print(next(myit))

class fruit:
    def __init__(self, mylist):
        self.mylist = mylist
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.mylist):
            item = self.mylist[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration


mylist = ["apple", "banana", "cherry"]
myclass = fruit(mylist)
myiter = iter(myclass)

for x in myiter:
    print(x)


class Alphabet:
    def __init__(self, start="A", end="Z"):
        self.start = ord(start)  # convert letter to ASCII  unicode
        self.end = ord(end)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            char = chr(self.start)  # convert ASCII back to letter
            self.start += 1
            return char
        else:
            raise StopIteration


Zoom = Alphabet()

for x in Zoom:
    print(x, end=" ")


def alphabet(n):
    if n > "Z":
        return "Z"
    else:
        print(n, end=" ")
        alphabet(chr(ord(n) + 1))


alphabet("A")


# polymorphism
class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("drive")


class boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("sail")


class plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly")


car1 = car("Ford", "Mustang")
boat1 = boat("Ibiza", "Touring 20")
plane1 = plane("Boeing", "747")

print("\n", car1.brand)

for x in (car1, boat1, plane1):
    print(x.brand, ":", x.model)
    x.move()


# having properties that can perform an action

class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = 50000  # A default value

    def give_raise(self, amount):
        self.salary *= amount
        print(f"{self.name}'s new salary is ${self.salary}")


# Creating instances (objects) of the Employee class
emp1 = Employee("Alice", "E123", "Engineering")
emp2 = Employee("Bob", "F456", "Finance")

emp1.give_raise(10000)  # Output: Alice's new salary is $60000
print(emp2.department)  # Output: Finance


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.is_logged_in = False

    def login(self):
        self.is_logged_in = True
        print(f"{self.name} is now logged in.")

    def logout(self):
        self.is_logged_in = False
        print(f"{self.name} is now logged out.")


# Usage is much cleaner and all related to the "User" concept


user1 = User("John", "john@example.com")
user1.login()


# Object_Oriented_Programming
# Encapsulation are related things(properties and method ) in a container (class)
# Name mangling with a double underscore to variable
# make it difficult to access outside a class ,
# but it possible to access with the class name by single underscore
# The double underscore is about safety from accidental mistakes,
# not absolute secrecy.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(self.__balance)

    def getbalance(self):
        return self.__balance


BA = BankAccount(50000)
BA.deposit(40000)

print(BA._BankAccount__balance)

# Abstraction focus on what an object does ,
# not how it does it,
# it is also hiding  the complex implementation details showing
# only the necessary features

from abc import ABC, abstractmethod


# in this below code @abstractmethod is used to enforce law on method
# so that I can use to them in subclass.
# the Abstract method is used to define the interface(design)


class Motor(ABC):  # Abstract class
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def turning(self):
        pass


class car(Motor):
    def __init__(self, oil, fuel):
        self.oil = oil
        self.fuel = fuel

    def move(self):
        if self.oil > 30:
            print("super cars are so fast ")

        else:
            print("This isn't a german car ")

    def turning(self):
        if self.fuel < 50:
            print("You need to fuel your car")
        else:
            print("speed up you  have alot of fuel")


Motors = car(50, 20)
Motors.move()
Motors.turning()


# Inheritance
class family56:
    def __init__(self, child17, child25):
        self.child17 = child17
        self.child25 = child25

    def firstborn(self):
        pass

    def second_born(self):
        pass


class SA(family56):
    def __init__(self, child17, child25):
        super().__init__(child17, child25)

    def firstborn(self):
        return f"Mr.Raheem SA first born is {self.child17}"

    def second_born(self):
        return f"Mr.Raheem SA Second born is {self.child25}"


Suraj = SA("Adedolapo", "Tomilola")
print(Suraj.firstborn())
print(Suraj.second_born())


# inheritance class polymorphism


class Animal:
    def speak(self):
        print("The animal makes a sound.")


class Dog(Animal):
    def speak(self):
        print("The dog barks.")


class Cat(Animal):
    def speak(self):
        print("The cat meows.")


animal = Animal()
dog = Dog()
cat = Cat()

for x in (animal, dog, cat):
    x.speak()

name = 'TutorialsPoint'
marks = 50
result = True


def myfunction():
    a = 10
    b = 20
    return a + b


# returns all the global name space in script
# print(globals())


def myfunc1():
    identity = "jane"

    def myfunc2():
        nonlocal identity
        identity = "hello, my name is jane"

    myfunc2()
    return identity


print(myfunc1())

var1 = 50  # this is a global variable
var2 = 60  # this is a global variable


def myfunction(x, y):
    global var1
    var1 = x
    global var2
    var2 = y
    total = x + y
    print("Total is a local variable: ", total)


myfunction(var1, var2)

import numpy as np
from learning import mode_modules, mode_modules as mm
mm.data['Hobbies'][4:6] = ["Basket Ball", "Boxing"]
my_hobbies = mm.data['Hobbies']
print(my_hobbies)

mm.myfunction(200, 150)

calculate = mm.calculator()
result = calculate.Adding(400, 200)
print(f"Stored values: {calculate.var1}, {calculate.var2}")

# create  a Numpy ndarray object
arr = np.array([10, 20, 30, 40, 50])
print(arr)

print(np.__version__)
arr = np.array([[7, 6, 5], [4, 5, 9]])
print(arr.dtype)
# inplace dtype(conversion)
arr_p= np.array(arr, copy=True, order="C",  ndmin=3, dtype=np.int8)
print(arr_p)
print(arr_p.dtype)
print("Shape: ", arr_p.shape)
print("Strides: ", arr_p.strides)
print("Item_size: ", arr_p.itemsize)

# create a structured Data Type
dt = np.dtype([("age", np.int8), ("love", "i8")])
print(dt)

# Applying Structured Data Type
# Each element of my array should not just be a number,
# but a record with a field named age
a = np.array([(10, 4), (20, 8), (30, 5)], dtype=dt)
print(a["love"])
print(a["age"])
# create a structured data type or record array
# using column input records
Data = np.dtype([("name", "S10"), ("Date", 'datetime64[m]'), ("country", ">U18")])
# Applying a structured data type
identity = np.array([("Adedolapo", np.datetime64("2025-08-28T10:30:10"), "Nigeria"),
                    ("Tomilola", np.datetime64("2025-08-29T11:30:10"), "Ghana"),
                    ("Kanisola", np.datetime64("2025-08-30T10:30:10"), "South Africa")
                     ], dtype=Data)
print(identity['name'])
print(identity['Date'])
print(identity['country'])

# convert Data Type
arr = np.array([1.1, 2.2, 3.3, 4.3])
new_arr = arr.astype(np.int64)
print(new_arr)
# numpy.cast
new_array = np.float32(new_arr)
print(new_array)
# view change the interpretation but not the underlying bytes
New_G = new_array.view(np.int32)
print(New_G)
print(New_G.itemsize)
# Numpy.array() is used to create an array
# Numpy.zero() is  used to create an array filled with zero (default float64)
arr = np.zeros((2, 3), dtype="i4", order='C')
print(arr)
# Numpy.ones() is used to create an array filled with one(default float64)
arr = np.ones((2, 2, 3), dtype="i4", order='C')
print(arr)

# numpy.arange() is generating a sequence of numbers based on
# specified start , stop  and step values
odd_arr = np.arange(1, 30, 2)
print("Odd :", odd_arr)

#Numpy.linspace() is used to create array by specifying the start,
# stop, and the number of elements we want
arr, step = np.linspace(1, 100, num=50, endpoint=True, retstep=True)
print(arr)
print("Step size: ", step)
# Numpy.random.rand is to generate numbers at random in an array
arr = np.random.rand(2, 3, 4)
print(arr)

#Numpy.empty() function by specifying the shape
# of the array as parameters.
arr = np.empty((3, 3), dtype=np.float64, order='C')
arr.fill(0)
print(arr)
arr[0, :] = [4, 3, 8]
arr[1, :] = [50, 20, 30]
arr[2, :] = [100, 130, 120]
print(arr)

#Numpy.full() : we can create an array with a desired shape and
# set all the elements in it to a specific value
arr = np.full((3, 3), 4, order="C")
print(arr)

# Numpy - Array Manipulation(Utilizes)
# reshape
arr = np.array([1, 5, 8, 9, 10, 12])
new_arr = arr.reshape(1, 2, 3)
print(new_arr)

# flat(attribute) iterator object
flat_arr = new_arr.flat
for f_r in flat_arr:
    print(f_r, end=" ")

# flatten()  Returns and collapsed into one dimension
arr = np.array(flat_arr)
new_arr = arr.flatten()
print("\nflatten: ", new_arr)

#ravel() Returns a contiguous flattened array
arr = new_arr.ravel()
print(arr)

# set
first_array = np.array([[12, 20, 30, 40]])
second_array = np.array([[20, 30, 15, 5]])
# in1d() : checking if the first array is present in the second array
if_present = np.in1d(first_array, second_array)
print(if_present)

#intersect1d(): find the common element in both array
if_com = np.intersect1d(first_array, second_array)
print(if_com)

#setdiff1d():Find the set difference of two arrays
# and returns the unique values in ar1 that are not in ar2
if_diff = np.setdiff1d(first_array, second_array)
print(if_diff)

#setxor1d():
#Find the set exclusive-or of two arrays and returns the sorted,
#unique values that are in only one (not both) of the input arrays
if_Tdiff = np.setxor1d(first_array, second_array)
print(if_Tdiff)

#union1d():
#Find the union of two arrays and returns the unique,
#sorted array of values that are in either of the two input arrays.
if_union = np.union1d(first_array, second_array)
print(if_union)

# Array from existing data
# asarray() converting a python object to an array
x = [4, "play", 587]
arr = np.asarray(x)
print(arr)

# numpy.frombuffer : this is useful when working with raw binary data
#A buffer object refers to a raw block of memory that holds
# binary data (bytes) without caring about its meaning or structure.
buff = b'My love for coding'
arr = np.frombuffer(buff, dtype='S2', offset=2)
print(arr)
# numpy.fromiter() function create a new
# one dimensional array from an iterable object


def generator(n):
    for i in range(n):
        yield i


arr = np.fromiter(generator(6), dtype=np.int32, count=3)
print(arr)
# python list
nested_list = [[1, 2, 3], [True, "Hello", 6], ['Ball', 8, 9]]
# this is a making a copy to store in a new memory (copy)
arr_from_nested_list = np.array(nested_list)

print("Array from nested list:")
print(arr_from_nested_list)
# this is a making a reference to same memory (view )
arr = np.asarray(arr_from_nested_list)
print(arr)
print(arr_from_nested_list is arr)

# iterating over Array
arr = np.array([[1, 4, 5, 6, 8], [7, 8, 9, 10, 12]])

for ar in arr:
    print(ar)

arr_3d = np.array([[[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]], [[10, 12, 13], [14, 11, 16], [21, 22, 23]]])

print(arr_3d.ndim)
print(arr_3d.shape)
for x in range(arr_3d.shape[0]):
    for y in range(arr_3d.shape[1]):
        for z in range(arr_3d.shape[2]):
            print(arr_3d[x, y, z])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
# using mutiple variable to get the  extract the shape of the array
rows, cols = arr_2d.shape

for i in range(rows):
    for j in range(cols):
        print(f"Element at ({i}, {j}):{arr_2d[i, j]}")

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in np.nditer(arr, flags=['external_loop']):
    print(x)

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])

# Modify array elements
with np.nditer(arr, flags=['buffered'], op_flags=['readwrite']) as it:
   for x in it:
      # Multiply each element by 2

      x[Ellipsis] = x * 2

print("Modified Array Example:",arr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
new_arr =arr.reshape(2, 5)
print(new_arr)


# concatening
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

arr3 = np.concatenate((arr1, arr2), axis= 1)
print("concatenate: ", arr3)

arr1 = np.array([1, 2, 3])
arr2 = np.array([[4, 5, 6], [7, 8, 9]])

# expand dimensions of arr1 to match the 2d array
expanded = np.expand_dims(arr1, axis=0)

con = np.concatenate((expanded, arr2), axis=0)
print(con)

# spliiting can only occur when they are even
# array_split allow when there is odd  split
"""
import numpy as np
arr = np.array([[4, 5, 6, 7, 9],
                [8, 2, 1, 3, 0]])
new_arr = np.array_split(arr, [2, 3], axis=1)
print(new_arr)

# horizontal splitting
arr = np.array([[4, 5, 6, 7, 9, 10],
                [21, 30, 40, 50, 55, 60],
                [8, 2, 1, 3, 0, 12]])
new_Hsplit = np.hsplit(arr, 3)
print("Hsplit : ", new_Hsplit)

# vertical splitting
new_Vsplit = np.vsplit(arr, 3)
print(new_Vsplit)

# Depth Splitting to split a 3D array along its
# third dimension
arr = np.arange(24).reshape(2, 3, 4)
new_Dsplit = np.dsplit(arr, 4)
print(new_Dsplit)

# flatten and ravel
new_ravel = np.ravel(new_Dsplit)
print(new_ravel)
new_ravel[4] = 500
print(new_ravel)

# recusion

def myfun(char):
    if char < 'A':
        return "A"
    else:
        print(char, end=" ")
        myfun(chr(ord(char) - 1))

myfun("Z")

def funtime(n):
    if n == 0 or n == 1:
        return 1

    else:
        result = n * funtime(n - 1)
        return result

print(funtime(6))


def dfum(k):
    if k > 0:
        result = k + dfum(k-1)
        return result
    else:
        result = 0
    return result
print(dfum(6))

"""
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibm = fib(n - 1) + fib(n - 2 )
        print(f"\n {n} = fib ({(n- 1)}) + fib({(n-2)}) = {fibm}")
        return fibm

fib(3)

"""
def fun_time(fib):
    if fib <= 1:
        return fib

    else:
        fib_m = fun_time(fib - 1) + fun_time(fib - 2)
        print(f"\nfib({fib})= fib({fib - 1}) + fib({fib - 2}) = {fib_m}")
        return fib_m

fun_time(5)

# generate a list with fibonacci
def fuck(n):
    sq = [0, 1]
    for x in range(2, n + 2):
        sq.append(sq[x-1] + sq[x -2])
    return sq

print(fuck(6))
Yup = [2, 3, 4, 7, 8]

fill = list(map(lambda x: x**2, filter(lambda x: x % 2 ==0, Yup)))
print(fill)
# ternary operation
grade = lambda score : "Pass" if score >= 70 else "fail" \
if score >= 45 else "work Hard"
print(grade(85))
print(grade(55))
print(grade(25))

from functools import reduce
fun = reduce(lambda j, k: j + k, Yup)
print(fun)

# currying with lambdas
create_email = lambda domain: lambda Username: f'{Username}@{domain}'
create_gmail = create_email('gmail.com')
create_company = create_email('company.com')
print(create_gmail('femi'))
print(create_company('jane'))

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  #private variable hidden

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def getbalance(self):
        self.__balance += 2000
        return self.__balance


BA = BankAccount(50000)
# bad practice
print(BA._BankAccount__balance)
print(BA.deposit(40000))
print(BA.getbalance())

from abc import ABC, abstractmethod

class kiss(ABC):
    @abstractmethod
    def Marry(self):
        pass

class Engage(kiss):
     def __init__(self, sex):
         self.sex = sex
     def Marry(self):
         print(f"When i {self.sex}  i will have alot sex" )


Danger = Engage('Marry')
Danger.Marry()

class donda:
    love = "Prayer the is master key "
    @staticmethod
    def Dun_time(k):
        print(k)
    @classmethod
    def time_up(cls):
        print(f" {cls.love}")

donda.Dun_time("Peace")
donda.time_up()

class Animal:
    def __init__(self, sound):
        self.sound = sound

    def speak(self,legs):
        print(f'Animal make {self.sound} with {legs}')


class cat(Animal):
            def __init__(self,sound, tail):
                super().__init__(sound)
                self.tail = tail

            def speak(self,mustache):
                print(f"Cat make a {self.sound} with a {self.tail}, they have {mustache}")


Big_cat = cat("Meow", "hairy tail")
Big_cat.speak("4 straight line mustache")


class Bird:
    def speak(self):
        print("Chirp")

class Cat:
    def speak(self):
        print("Meow")

Big = Bird()
Big_C = Cat()
for animal in [Big, Big_C]:
    animal.speak()


class Employee:
    company = "Google"  # Class variable (shared)

    #def __init__(self, name):
    #    self.name = name

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name  # modifies class variable


# Use it
Employee.change_company("OpenAI")
print(Employee.company)  # ✅ Output: OpenAI


from abc import ABC, abstractmethod

# 🧠 1. Abstraction (abstract class)
class BankAccount(ABC):
    def __init__(self, owner, balance):
        # 🔒 2. Encapsulation (private variable)
        self.__owner = owner
        self.__balance = balance

    # 🧩 3. Abstraction (must be implemented by subclasses)
    @abstractmethod
    def account_type(self):
        pass

    # Public method to safely access balance
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}, new balance is {self.__balance}")

# 🧬 4. Inheritance (subclass inherits from BankAccount)
class SavingsAccount(BankAccount):
    def account_type(self):
        print("Savings Account")

# 🧬 Another subclass to show Polymorphism
class CurrentAccount(BankAccount):
    def account_type(self):
        print("Current Account")

# 🎯 Create objects
s1 = SavingsAccount("Alice", 5000)
c1 = CurrentAccount("Bob", 8000)

# 👇 Polymorphism: same method, different behavior
for acc in [s1, c1]:
    acc.account_type()

# Encapsulation & Abstraction
s1.deposit(2000)
print(s1.get_balance())  # Accessing safely

# multiple inheritance
class division:
    def __init__(self, a , b):
        self.a = a
        self.b = b
    def divide(self):
        return self.a // self.b

class modulus:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def mod(self):
        return self.a % self.b

class div_mod(division,modulus):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __divmod__(self, other):
        divval = self.a // other.a
        modval = self.b % other.b
        return (divval, modval)

x = div_mod(20, 6)
y = div_mod(6, 3)
print(f"Division :{x.divide()}")
print(f"Modulus :{x.mod()}")
print(f"Div__Mod :{divmod(x, y)}")

print(div_mod.mro())

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    def show(self):
        print("Class D")
        super().show()

d = D()
d.show()
# polymorphism
# duck typing
class Duck:
   def sound(self):
      return "Quack, quack!"

class AnotherBird:
   def sound(self):
      return "I'm similar to a duck!"

def makeSound(tuck):
   print(tuck.sound())

# creating instances
duck = Duck()
anotherBird = AnotherBird()
# calling methods
makeSound(duck)
makeSound(anotherBird)

# method overiding
from abc import ABC, abstractmethod
class shape(ABC):
   @abstractmethod
   def draw(self):
        return "Abstract method"


class circle(shape):
   def draw(self):
       #msg = super().draw()
       #print(msg)
       print ("Draw a circle")
       return

class rectangle(shape):
   def draw(self):
      print(super().draw())
      print ("Draw a rectangle")
      return

shapes = [circle(), rectangle()]
for shp in shapes:
   shp.draw()

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __str__(self):
        #return 'Vector (%d, %d)' % (self.a, self.b)
        return f"Vector : {(self.a, self.b)}"

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Vector(self.a * other.a, self.b * other.b)


w = int(input("Enter a value :  "))
x = int(input("Enter a value :  "))
y = int(input("Enter a value :  "))
z = int(input("Enter a value :  "))

V1 = Vector(w,x)
V2 = Vector(y, z)
print(V1 + V2)
print(V1 * V2)
"""
v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
"""
# method overloading
class Example:
    def greet(self, name=None):
        if name:
            print(f"Hello, {name}")
        else:
            print("Hello")

obj = Example()
obj.greet()
obj.greet("Raheem")

#multi level inheritance
class Network:
    def connectivity(self):
        return "Network connects"

# Derived class
class Network_5G(Network):
    def fast_connectivity(self):
        return "5G Network provides superfast connectivity"

    def connectivity(self):
        return "5G Network connects faster"

# Sub-derived class
class Network_5G_Airtel(Network_5G):
    def fast_and_stable_connectivity(self):
        return "Airtel 5G network is fast and remains stable"

# Creating an instance of Network_5G_Airtel
obj1 = Network_5G_Airtel()
print(obj1.connectivity())  # Inherited from Network class
print(Network_5G_Airtel.mro())

class Parent:
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ("Calling parent method")

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

# define child class
class Child(Parent):
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ("Calling child method")

# instance of child
P = Parent()
c = Child()
# child calls its method
#c.childMethod()
# calls parent's method
#c.parentMethod()
# again call parent's method
#c.setAttr(200)
# again call parent's method
#c.getAttr()
print(V1.__dict__)

import sys
# Create object <40>
a = 40
# Increase ref. count  of <40>
b = a
# Increase ref. count  of <40>
c = b
print(sys.getrefcount(a))
# Decrease ref. count  of <40>
del a
# Decrease ref. count  of <40>
b = 100
# Decrease ref. count  of <40>
#c[0] = -1
print(b)
#print(c)

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
# prints the ids of the obejcts
print (id(pt1), id(pt2), id(pt3)) #all same ID -> same object
print(sys.getrefcount(pt1))
del pt1
del pt2
del pt3
# modify cant occur in static method but it possible through
# constructor
# and that isnt the main impoatance of static in this example ,
# it used for utility function /helper function
class Cloth:
    brandname = "Name of the brand is Raymond"
    def __init__(self):
        Cloth.brandname = "Demiestudios is the name of the brand"
    @staticmethod
    def Brand():
        print(Cloth.brandname)
c = Cloth()
c.Brand()

# Using private Access modifier
# and property decorater to get the private instance variable
class road:
    def __init__(self, state, capital):
        self.__state = state
        self.__capital = capital
    @property
    def retrieve_sc(self):
        return f"{self.__state} :{self.__capital}"
    @retrieve_sc.setter
    def retrieve_sc(self,values):
        self.__state, self.__capital = values

    @retrieve_sc.deleter
    def retrieve_sc(self):
        pass
Road = road("Lagos", "Ikeja")
print(Road.retrieve_sc)

Road.retrieve_sc =("Oyo", "Ibadan")
print(Road.retrieve_sc)


class Employee:
    def __init__(self):
        self.name = "Bolu"
        self.age = 30

    def med(self):
        print(f"Name :{self.name}\nAge: {self.age}")

emp = Employee()
emp.med()
#method overloading
class example:
    def add(self, a = None, b = None, c = None):
        if a != None and b !=None and c != None:
            x = a + b + c
            return x
        elif a!= None and b != None  and c == None:
            x =a + b
            return  x

exam = example()
print(exam.add(20, 40, 50))
print(exam.add(40, 50))

from multipledispatch import dispatch
class example :
    @dispatch(int, int)
    def add (self, a, b):
        x = a + b
        return x
    @dispatch(int, int, float)
    def add(self, a, b, c):
        x = a + b + c
        return x
exam = example()
print(exam.add(20, 40 , 60.5))
print(exam.add(50, 60))

class file :
    def generate(self):
        print('This a pdf file')

class B_file:
    def generate(self):
        print('The is a execl file')

def summit(vile):
    vile.generate()

File = [file(), B_file()]

for B in File:
    summit(B)

class University:
    def __init__(self, name):
        self.name = name
    def uni(self):
        return f"i finised my Diploma at {self.name}"

    class Niche:
        def __init__(self, department):
            self.department = department
        def wip(self):
            return f"Learning {self.department}"
Big_uni = University("APTECH")
CM = University.Niche("Data Science")
print(Big_uni.uni())
print(CM.wip())

# multiple inner class
# A single outer class contain more than one inner class
class Organization:
    def __init__(self):
        self.inner1 = self.Department1()
        self.inner2 = self.Department2()
    def showName(self):
        print("Organization: Kipsy Tea")

    class Department1:
        def display(self):
            print("The processing dept")

    class Department2:
        def display2(self):
            print("The packing dept")
# instance of the outer class
organ = Organization()
# instance of the inner class , because they it a nested class
cm = organ.Department1()
cm2 = organ.Department2()
# calling the method
organ.showName()
cm.display()
cm2.display2()

# multilevel inner class
class Organization:
   def __init__(self):
      self.inner = self.Department()

   def showName(self):
      print("Organization Name: Tutorials Point")

   class Department:
      def __init__(self):
         self.innerTeam = self.Team1()

      def displayDep(self):
         print("In Department")

      class Team1:
         def displayTeam(self):
            print("Team 1 of the department")

 # instance of the outer class
outer= Organization()
# calling the method outer class
outer.showName()
# inner class instance
inner = outer.inner
inner.displayDep()

# Access Team1 instance
innerTeam = inner.innerTeam
# Calling display method
innerTeam.displayTeam()


