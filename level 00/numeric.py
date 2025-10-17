#Generate a random integer between 1 and 100 , and check if the results is an even number 
import random
ran = random.randint(1,100)
print(ran)
if ran % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")




