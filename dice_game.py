import random 

def roll_dice(num_dice):
    return [random.randint(1,6) for _ in range(num_dice)]
print("=== Dice Rolling Game ===")
name = input("What's your name?  ").strip() or "Player"
print(f"Welcome {name}!\n")

num_dice = int(input("How many dice would you like to roll?  "))

roll_count = 0 

while True:
    print("\nMenu: [R] Roll  [Q] Quit")
    choice = input("Choose an option: ").strip().lower()

    if choice == "r":
        results = roll_dice(num_dice)
        roll_count += 1
        total = sum(results)
        print(f"You rolled: {' '.join(str(x) for x in results)} | total ={total}")
        print(f"Rolls this session: {roll_count}")
    elif choice == "q":
        print(f"Thanks for playing , {name}! total rolls : {roll_count}")
        break
    else:
        print("Please choose R or Q.")

