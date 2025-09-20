""" text = "Accounting"
print(len(text))
print(len(text.strip()))

nm_of_space = len(text) - len(text.strip())
is_data_clean = len(text) == len(text.strip())
print(f"Nm of Spaces is {nm_of_space}")
print(f"Is data clean : {is_data_clean}")"""

raw_data = "968-Maria,( D@t@ Engineer );; 27y  "

name = raw_data.lower().lstrip("968-").strip("( d,( D@t@ Engineer );; 27y  ")
role = raw_data.lower().lstrip("968-maria,( ").rstrip(" );; 27y  ").replace("@","a")
age = raw_data[30:32]
print(f"name : {name} | role : {role} | age : {age}")
#print(f"role : {role}")

