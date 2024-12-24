from math import prod

def factorial_prod(n):
    return prod([i for i in range(1, n + 1)])

n = int(input("Enter a number: "))
print(f"The factorial of {n} is {factorial_prod(n)}")
