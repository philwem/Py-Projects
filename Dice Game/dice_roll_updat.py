import random  # Import the random module to generate random numbers

# Function to roll a specified number of dice
def roll_dice(num_dice):
    results=[]  # List to store each die result
    for _ in range (num_dice):  # Loop runs for the number of dice specified
        results.append(random.randint(1,6)) # Generate number between 1 and 6 and add to results
        # Print results as space-separated values
        print("You rolled:"," ".join(str(die) for die in results))

# Ask the user how many dice they want to roll        
while True:
    try:
        num_dice = int(input("How many dice wouls you like to roll? "))# Get number of dice from user
        if num_dice <= 0: # Check if the number is valid (positive)
            print|("Please enter a positive number.")
            continue # Restart loop if invalid
        break # Exit loop if valid
    except ValueError:  # Handle case where input is not a numbe
        Print("Please enter a valid number.")
# Counter to keep track of rolls
roll_count = 0

# Main rolling loop
while True:
    roll_dice(num_dice) # Roll the dice
    roll_count += 1  # Increment roll counter
    print(f"Roll count : {roll_count}")# Show how many rolls so far

    choice = input("Roll again? (y/n): ").strip().lower() # Ask user if they want to roll again
    if choice != 'y': # If answer is not 'y', exit the game
        print(f"Thanks for playing! You rolled the dice {roll_count} times in total")
        break # Stop the loop