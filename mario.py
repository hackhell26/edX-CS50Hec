from cs50 import get_int

def main():
    height = get_height()
    for i in range(height):
        print("#")

def get_height():
    while True: # do while loop doesn't exist in python
        n = get_int("Height: ") # do whatever you have to do
        if n > 0: # and if it is that what i want, break the program
            break
    return n

main()