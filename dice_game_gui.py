import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox #
import random

#Create main window
root = tk.Tk()
root.title("Dice game challenge")
root.configure(bg="#2c3e50")

#Load dice images into list
dice_image = []
for i in range(1, 7):
    img = Image.open(f"dice{i}.png")  # open image
    img = img.resize((100, 100))       # resize to 100x100 px
    dice_image.append(ImageTk.PhotoImage(img)) #store as photoimage

#Roll counter
roll_count = 0
#
win_count = 0
target_total = 7 # Default target

#Function to rolldice
def roll_dice():
    global roll_count , win_count
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll_count += 1
#Update dice image
    dice_label1.config(image=dice_image[roll1 - 1])
    dice_label2.config(image=dice_image[roll2 - 1])

    total = roll1 + roll2
    total_label.config(text=f"Total: {total}")
    counter_label.config(text=f"Rolls: {roll_count}")

    if total == target_total:
        win_count += 1
        win_label.config(text=f"Wins: {win_count}")
        messagebox.showinfo("🎉 You Win!", f"You hit the target {target_total} in {roll_count} rolls!")
   
def set_target():
    global target_total
    try:
        target_total = int(target_entry.get())
        target_label.config(text=f"Target: {target_total}")
    except ValueError:
        target_label.config(text="Target: Invalid")

# Frame for dice images
dice_frame = tk.Frame(root, bg="#2c3e50")
dice_frame.pack(pady=10)

# First dice
dice_label1 = tk.Label(dice_frame, image=dice_image[0],bg="#2c3e50")
dice_label1.pack(side="left", padx=5)

# Second dice
dice_label2 = tk.Label(dice_frame, image=dice_image[0],bg="#2c3e50")
dice_label2.pack(side="left", padx=5)

# Labels
total_label = tk.Label(root, text="Total: 2", font=("Arial", 16),fg="white", bg="#2c3e50")
total_label.pack()

counter_label = tk.Label(root, text="Rolls: 0", font=("Arial", 14),fg="white", bg="#2c3e50")
counter_label.pack()

win_label = tk.Label(root, text="Wins: 0", font=("Arial", 16), fg="white", bg="#2c3e50")
win_label.pack()

target_label = tk.Label(root, text=f"Target: {target_total}", font=("Arial", 16), fg="yellow", bg="#2c3e50")
target_label.pack()

# Target input
target_entry = tk.Entry(root, font=("Arial", 14))
target_entry.pack(pady=5)

set_button = tk.Button(root, text="Set Target", command=set_target, font=("Arial", 14), bg="#27ae60", fg="white")
set_button.pack(pady=5)

#Roll button
roll_button = tk.Button(root, text="Roll dice", command=roll_dice, font=("Arial",14), bg="#2980b9",fg="white")
roll_button.pack(pady=10)

root.mainloop()











































# import tkinter as tk  # Import Tkinter Library
# import random # We'll need this for rolling the dice


# #Function to roll dice (placeholder for now)
# def roll_dice():
#    dice_value = random.randint(1, 6)# Get a random number between 1 and 6
#    result_label.config(text=f"You rolled: {dice_value}") # update label text

# #Create the main window
# root = tk.Tk()
# root.title("Dice Game")  # Set window title
# root.geometry("400x300") # Set window size (width x height)

# #Lalel to display result 
# result_label = tk.Label(root, text="Click Roll Dice to start", font=("Arial",16))
# result_label.pack(pady=20)



# # Add a roll dice button
# roll_button = tk.Button(root,text="Roll dice",font=("Arial",16), command=roll_dice)
# roll_button.pack(pady=20) # Add padding so it's not stuck to the top

# # Keep the window open
# root.mainloop()