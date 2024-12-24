from functools import reduce

def reverse_string_reduce(s):
    return reduce(lambda x, y: y + x, s)

string = input("Enter a string: ")
print(f"Reversed string: {reverse_string_reduce(string)}")