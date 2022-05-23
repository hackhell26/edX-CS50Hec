from cs50 import get_string

before = get_string("Before: ")
print("After: ", end="")

for c in before:    # for c in the string in question
    print (c.upper(), end="")   # c = especific character
print()
