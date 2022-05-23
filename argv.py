from sys import argv #argv it is a list

for arg in argv[1:]: # slicing the argv list, starting at position 1 going all of the way to the ende
    if arg != "argv.py":
        print(arg)