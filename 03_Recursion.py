# Recursion---> When we call a Fuction inside the same Fuction.

# Factorial
def factorial(n):
    if (n==0 or n==1 ):
        return 1
    else:
        return n * factorial(n-1) 

print(factorial(5)) 

#  Fibonacci sequence
def F(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return F(n-1) + F(n-2)

print(F(6)) 