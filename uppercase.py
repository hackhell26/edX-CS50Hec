from cs50 import get_string

before = get_string("Before: ")
after = before.upper()      # calling upper() to whole string, not one character at a time
print (f"After: {after}")   # not need it the (end="") because i'm printing the whole
# thing out once, not character by character, and the print() line ether
