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
