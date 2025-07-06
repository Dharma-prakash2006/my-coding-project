print("Hello, World!")
a = 5
b = 10
c = a + b
print(c)
def greet(name):
    return f"Hello, {name}!"    
print(greet("Alice"))
def add(x, y):              
    return x + y
print(add(3, 4))
def multiply(x, y):
    return x * y
print(multiply(2, 3))
def subtract(x, y):

    return x - y
print(subtract(10, 4))
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y
print(divide(10, 2))
def power(x, y):        
    return x ** y
print(power(2, 3))
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result