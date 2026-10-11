import random

print("1. Generating Numbers")
print(f"Random Float (0.0-1.0): {random.random()}")

print(f"Random Float (10.5-25.5): {random.uniform(10.5, 25.5)}")

print(f"Random Integer (1-6): {random.randint(1,6)}")

print(f"Random Even Number (0-10): {random.randrange(0,11,2)}")

print("2. Working With Lists")
fruits = ['apple', 'banana', 'cherry', 'date']

print(f"Single Choice: {random.choice(fruits)}")

print(f"Choices (wth duplicates): {random.choices(fruits, k=3)}")

print(f"Sample (unique): {random.sample(fruits, k=3)}")

print("3. Shuffle Cards")
cards = ['ace', 'king', 'queen', 'jack']
random.shuffle(cards)
print(f"Shuffled Cards: {cards}\n")