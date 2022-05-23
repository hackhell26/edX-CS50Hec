from sys import argv #argv it is a list

for arg in argv: # for loop to print out all the CLI arguments that i type in
    if arg != "argv.py":
        print(arg)