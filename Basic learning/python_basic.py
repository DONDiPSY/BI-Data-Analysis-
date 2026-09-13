#Variables and data types
#Loops
#Functions
#Object-Oriented Programming (OOP)
#Exception handling
#Modules and packages
#File handling
#Virtual environments


#Variables and data types
x = 5
print(x)

y = "sallay" # y is a string
x, y, z = "orange", "Banana", "cherry"
print(x)
print(y)
print(z)

x = "orange"
y = x
z = y

x = "awesome"

def myfunc():
    x = "fantastic"

myfunc()
print("Python is " + x)

# data types

#Loops
# while loop  using contiue
i  =  0
while i < 6 :
    i += 1
    if i == 3:
        continue
    print(i)
# while loop using break
i = 1
while i < 5 :
    print(i)
    if i == 3:
        break
    i += 1

# for loop when x is banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break



fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)



Names = ["Ayodeji", "Tomilola", "Kayode"]
surname  =  ["Dipsy", "Raheem", "oke"]
for x in Names:
    for y in surname:
        print(x,"--",y)


while (line := input("Enter a line or exit to quite: ")) != "exit":
    print(f"You entered : {line}")

# functions
def  Organize(arg):
    print("ID inside the function: ", id(arg))
var = "Hello"
print("ID before passing: ",id(var))
Organize(var)

def greetings(name):
    print(f"Hello {name}")

greetings("Adedolapo")

# default and keyword Argument
def printinfo (name , age =30):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return;

# call the printinfo function
printinfo(age=50, name="Tomilola" )
printinfo(name="Ayodeji")

# postional-only argument
def postion(a, b, /):
    print(f"Adedolapo is an expert in {a}\n"
          f"Tomilola is {b}\n"
          )
    return ;
postion("Data Engineer", "Creative")

def multiply(x, y):
    z = x * y
    print(f"a = {x} b = {y} result = {z}")
    return z
a = 10
b = 20
result = multiply(a,b)

def multiply():
    z = lambda j, k: j * k
    a, b = 10, 5
    print(f"a = {a} b = {b} result = {z(a, b)}")
    return z

multiply()

marks = 50
def myfunc():
    global marks
    marks = marks + 20
    print(marks)
myfunc()

var1 = 60
var2 = 60
def myfunc(x, y):
    global total
    total = x * y

myfunc(var1, var2)
print(total)

# decoretor
# The function changecase is the decorator
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
# The function myfunc
# is the function that gets decorated.
@changecase
def myfunc():
    return "hello sally"
print(myfunc())

def upper(f):
    def myinner():
        return f().upper()
    return myinner
def exclaim(f):
    def myinner():
        return f() + "!"
    return myinner
@upper
@exclaim
def processed():
    return "hi"
print(processed())

def myfunction(a: int, b: int) -> int :
    c = a + b
    return c
print(myfunction(40, 50))
print(myfunction.__annotations__)

def is_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)


is_even([5, 6, 4, 8, 3, 1])


def is_prime(numbers):
    result = []
    # iterate through a the result list
    for num in numbers:
        # check if num is less than 1 then skip
        if num <= 1:
           continue
        dprime = True
        # check for factors from 2 up to sqrt(num) and increment by 1
        for divisor in range (2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                dprime = False
                # stop item from appending to result if num isn't prime number
                break
        if dprime:
                result.append(num)
    return result

prime = is_prime([1, 2, 5, 6, 7, 9, 4, 8, 3, 1])
print(prime)

