from cs50 import get_string

# the idea in this is associate keys with values
people = {
    "Hector" : "666196831",
    "Dayana" : "04141565657"
}

name = get_string("Name: " )
if name in people:
    print(f"Number: {people[name]}")
    exit(0)

print("Not found")
exit(1)