import random 

def roll_dice(num_dice):
    return [random.randint(1,6) for _ in range(num_dice)]
print("=== Dice Rolling Game ===")
name = input("What's your name?  ").strip() or "Player"
print(f"Welcome {name}!\n")

roll_count = 0 
roll_history = []
high_score = 0 


print("Welcome to the Dice Rolling Game!")
print("Type 'r' to roll, 'h' to see history, or 'q' to quit.")

while True:
    choice = input("\nEnter your choice (r/h/q): ").lower()

    if choice == "r":
        # Ask how many dice to roll
        num_dice = int(input("How many dice do you want to roll? "))

        # Ask the player how many sides each die has
        num_sides = int(input("How many sides should each die have? "))

        # Roll the dice
        results = [random.randint(1, 6) for _ in range(num_dice)]
        total = sum(results)

        dice = [random.randint(1, num_sides) for _ in range(num_dice)]
        print(f"You rolled: {dice}")

        print(f"You rolled: {results}")
        print(f"Total: {total}")

        # Save this roll to history
        roll_history.append((results, total))

        # Track high score
        current_high = max(dice)
        if current_high > high_score:
            high_score = current_high
            print(f"🎉 New high score: {high_score}!")
        else:
            print(f"Current high score: {high_score}")


        roll_count += 1
        print(f"You have rolled {roll_count} time(s) this session.")



    elif choice == "h":
        if not roll_history:
            print("No rolls yet!")
            print(f"Total rolls so far: {roll_count}")

        else:
            print("\n--- Roll History ---")
            for i, (rolls, total) in enumerate(roll_history, start=1):
                print(f"{i}. Rolled: {' '.join(str(x) for x in rolls)} | Total = {total}")

    elif choice == "q":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice, please enter 'r', 'h', or 'q'.")

