import random
def roll_dice():
    # Generate two random numbers between 1 and 6
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  print(f"You rolled: {die1} and {die2}")

# Main loop
while True:
  roll_dice()
  choice = input("Roll again? (y/n):").strip().lower()
  if choice != 'y':
    print("Thanks for playing")
    break