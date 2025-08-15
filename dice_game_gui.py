import tkinter as tk
from PIL import Image, ImageTk
import random

#Create main window
root = tk.Tk()
root.title("Two Dice Game")

#Load dice images into list
dice_image = []
for i in range(1, 7):
    img = Image.open(f"dice{i}.png")  # open image
    img = img.resize((100, 100))       # resize to 100x100 px
    dice_image.append(ImageTk.PhotoImage(img)) #store as photoimage

#Roll counter
roll_count = 0

#Function to rolldice
def roll_dice():
    global roll_count
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll_count += 1
#Update dice image
    dice_label1.config(image=dice_image[roll1 - 1])
    dice_label2.config(image=dice_image[roll2 - 1])

# Frame for dice images
dice_frame = tk.Frame(root)
dice_frame.pack(pady=10)

# First dice
dice_label1 = tk.Label(dice_frame, image=dice_image[0])
dice_label1.pack(side="left", padx=5)

# Second dice
dice_label2 = tk.Label(dice_frame, image=dice_image[0])
dice_label2.pack(side="left", padx=5)

# Total label
total_label = tk.Label(root, text="Total: 2", font=("Arial", 14))
total_label.pack()

# Roll counter label
counter_label = tk.Label(root, text="Rolls: 0", font=("Arial", 14))
counter_label.pack()

#Roll button
roll_button = tk.Button(root, text="Roll dice", command=roll_dice, font=("Arial",14))
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