from cs50 import get_int

scores = [] # This is a empty list or empty array
for i in range(3):
    score = get_int("Score: ")
    scores.append(score)

average = sum(scores) / len(scores)
print(f"Average: {average}")
