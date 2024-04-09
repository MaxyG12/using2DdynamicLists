print("David's Nan's Bingo Card Generator")
print()

import random

def ran():
    number = random.randint(1, 90)
    return number

def prettyPrint():
    for row in bingo:
        print(row)

numbers = []
for i in range(8):
    numbers.append(ran())
numbers.sort()

bingo = [
    [numbers[0], numbers[1], numbers[2]],
    [numbers[3], "BINGO", numbers[4]],
    [numbers[5], numbers[6], numbers[7]]
]

# Randomly select 3 distinct numbers (excluding BINGO)
selected_indices = random.sample(range(8), 3)
for idx in selected_indices:
    row, col = divmod(idx, 3)
    bingo[row][col] = "X"

# User guessing loop
for _ in range(3):
    prettyPrint()
    print()
    guess = int(input("Guess the original number (1-90): "))
    if guess in numbers:
        print("Correct! You guessed one.")
        numbers.remove(guess)
    else:
        print("Incorrect. Try again.")

# Check if the user guessed all three correctly
if len(numbers) == 0:
    print("Congratulations! You've won!")
else:
    print("Better luck next time!")

  
    








