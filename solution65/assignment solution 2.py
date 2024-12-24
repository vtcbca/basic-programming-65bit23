import sympy

def is_prime_sympy(n):
    return sympy.isprime(n)

n = int(input("Enter a number: "))
print(f"Is {n} prime? {is_prime_sympy(n)}")