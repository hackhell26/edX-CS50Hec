import sys

# Linear search
numbers = [26, 15, 7, 10, 4, 3, 39, 0]

if 15 in numbers:
    print("found")
    sys.exit(0)

print("Not found")
sys.exit(1)
