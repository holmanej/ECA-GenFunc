import sympy as sy
import numpy as np

# Define the variable and the function to approximate
x = sy.Symbol('x')
f = -1 / ((x - 1)*(x**2 + 1))


# Factorial function
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)

# Taylor approximation at x0 of the function 'function'
def taylor(function,x0,n):
    i = 0
    p = 0
    while i <= n:
        p = p + (function.diff(x,i).subs(x,x0))/(factorial(i))*(x-x0)**i
        i += 1
    print(p)
    return p

taylor(f, 0, 7)