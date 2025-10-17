number = "+49 (176) 123-4567"

print(number.replace("+","00").replace(" ","").replace("(","").replace(")","").replace("-",""))


# f string

name = "Philip Mawuli"
age = 24 
is_student = False 

print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")

# Split()

csv_file = "1234,Adu,Ghana,1999-08-04,Male"
print(csv_file.split(","))