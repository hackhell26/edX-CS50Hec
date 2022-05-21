from cs50 import get_int

# validation for no positive numbers
while True: # do while loop doesn't exist in python
    n = get_int("Height: ") # do whatever you have to do
    if n > 0: # and if it is that what i want, break the program
        break

for i in range(n):
    print("#")
