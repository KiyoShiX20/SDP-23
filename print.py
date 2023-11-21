def function_():
    print(1,2,3,4, sep="#", end="&\n")
    x = True
    print(x, "is of type",type(x))
function_()

a = "hello"
print(a, "is of type", type(a))
print(a, "is of type", type(a), isinstance(a, int))
print("hello")
fruits = []
fruits.insert(1, "Apple")
fruits.insert(2, "Mango")
fruits.insert(0, "Orange")
del fruits[0]
fruits.clear()
print(fruits)

m_tuple = ["abc", 123, "IIIIII"]
print(m_tuple)
print(m_tuple[1:3])
print(m_tuple[-1])
print(m_tuple[-2])
print(m_tuple[-3])

m_set_a = {1, 2, 3, 4}
m_set_b = {4, 5, 6}
print(m_set_a.intersection(m_set_b))
print(m_set_a.union(m_set_b))
print(m_set_a.symmetric_difference(m_set_b))

class Person:
   def __init__ (self, name, age, gender):
       self.name = name
       self.age = age
       self.gender = gender

obj = Person("Aravind", 45, "Male")
print(obj.name, obj.age, obj.gender)
print(obj.name is not obj.age)
print(obj.name is obj.age)
print(obj.age is obj.age)
if (obj.age is obj.age):
    print("Age is Age")
else:
    print("Age is not Age")

if (obj.age is not obj.age):
    print("Age is not Age")
elif (obj.age is obj.age):
    print("Age is Age")
else:
    print("Something else")

# Given number is odd or even
def oddeven (x):
    if x%2 == 0:
        print(x, "is even")
    else:
        print(x, "is odd")

# Given year is leap year
def leap(x):
    if x%4 == 0:
        print(x, "is a leap year")
    else:
        print(x, "is not a leap year")

# Given number is divisible by 7
def seven(x):
    if x%7 == 0:
        print(x, "is divisible by 7")
    else:
        print(x, "is not divisible by 7")

# Read 3 numbers and finf the sum and average
def rsa():
    storage=[] 
    for i in range(0, 3):
        x = input()
        storage[i] = x

    for i in range(0, 3):
        sum += storage[i]

    avg = sum / 3

    print(storage)
    print(sum)
    print(avg)

# Read 3 marks and pass or fail
def passfail():
    storage=[] 
    for i in range(0, 3):
        x = input()
        storage[i] = x

    for i in range(0, 3):
        if(storage[i] < 40):
            print(i, "=> Fail")
        else:
            print(i, "=> Pass")

# Check for vowel
def vowel():
    x = input()
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        print(x, "is a vowel")
    else:
        print(x, "is not a vowel")

oddeven(2354453)
leap(2024)
seven(21)
#rsa()
#passfail()
#vowel()  


#few more questions
def onetofifty():
    for i in range(1, 51):
        print(i)

def multitable(x):
    for i in range(0, 11):
        print( i * x)

def factorial(x):
    fact = 1
    while(x != 0):
        fact *= x
        x -= 1

def reverse(x):
    rev = 0
    while(x != 0):
        rev = (x%10) + rev * 10
        x = x//10
    print(rev)

def prime(x):
    for i in range(2, x):
        if(x%i == 0):
            print(x, "is a prime number")
            break
    else:
        print(x, "is not a prime number")

def triangle1(n):
    for i in range (1, n):
        for j in range (1, n):
            if(j <= i):
                print(j, end="")
            else:
                print(end=" ")
        print("\n")

def triangle2(n):
    for i in range (1, n):
        for j in range (1, n):
            if(j <= i):
                print(i, end="")
            else:
                print(end=" ")
        print("\n")

def triangle3(n):
    for i in range (1, n):
        for j in range (1, n):
            if(j <= i):
                print(n-i, end="")
            else:
                print(end=" ")
        print("\n")

def triangle4(n):
    for i in range (1, n):
        for j in range (1, n):
            if(j <= i):
                print(n-j, end="")
            else:
                print(end=" ")
        print("\n")

def triangle5(n):
    for i in range (1, n):
        for j in range (1, n):
            if(j <= i):
                print('*', end="")
            else:
                print(end=" ")
        print("\n")

def triangle6(n):
    for i in range (1, n):
        for j in range (1, n):
            if(j <= i):
                print(end=" ")
            else:
                print('*', end="")
                
        print("\n")

def triangle6(n):
    pTriangle = [] 
    for i in range(n): 
        row = [1] * (i + 1) 
        for j in range(1, i):
            row[j] = pTriangle[i - 1][j - 1] + pTriangle[i - 1][j] 
        pTriangle.append(row) 
    return pTriangle
                


onetofifty()
factorial(5)
multitable(5)
reverse(1234898181939)
prime(21)
prime(11)
triangle1(5)
triangle2(5)
triangle3(5)
triangle4(5)
triangle5(5)
triangle6(5)

