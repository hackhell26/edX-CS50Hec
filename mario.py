
def main():
    height = get_height()
    for i in range(height):
        print("#")

def get_height():
    while True: # do while loop doesn't exist in python
        try:
            n = int(input("Height: ")) # do whatever you have to do
            if n > 0: # and if it is that what i want, break the program
                break
        except ValueError:
            print("That's not an integer")
    return n

main()