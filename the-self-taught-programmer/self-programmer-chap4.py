#Chapter 4 challenges

#challenge 1
"""
Takes a number as an input and returns that number squared
:n gets input from user
:Returns input to the second power
:Print fun function with user input as parameter
"""
n = int(input("Enter a number: "))
def fun(n):
    return n**2
print(fun(n))

#challenge 2
"""
Accepts a string as a parameter and prints it
:Word gets string
:Function accepts word
:Print word
:Call function
"""
word = "This is a string"
def accept(word):
    print(word)
accept(word)

#challenge 3
"""
Function takes 3 required functions and 2 optional functions
:takes has 5 parameters; first 3 required and last 2 optional
:Returns parameters (a+b+c) plus (d+e)
:Print function with first three arguments; purposely omits optional one
"""
def takes(a, b, c, d=1, e=2):
    return((a+b+c)+(d+e))
print(takes(1,2,3))

#challenge 4
"""
Program with two functions.
First function takes an integer as a parameter:
:Returns parameter divided by 2 to get the quotient
:Save function to variable

Second function:
:Assign y to variable
:Pass y as parameter
:Return parameter muliplied by 4
:Prints second function w/ y as argument
"""
x = 10
def fun1(x):
    return x // 2
result1 = fun1(x)

y = result1
def fun2(y):
    return y * 4
print(fun2(y))

#challenge 5
"""
Function coverts a string to a float
:Pass parameter to convert function
:Returns c as a parameter of float
:Prints convert function with arguments
"""
def convert(c):
    return float(c)
print(convert("55"))

#challenge 6
"""Add Docstring to challenges 1 - 5"""
