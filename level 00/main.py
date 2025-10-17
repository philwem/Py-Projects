```python
text = "Accounting"
# Calculate the number of leading/trailing spaces in the string.
num_spaces = len(text) - len(text.strip())
# Check if the string has any leading/trailing spaces.
is_clean = num_spaces == 0

print(f"Number of spaces: {num_spaces}")
print(f"Is data clean: {is_clean}")

raw_data = "968-Maria,( D@t@ Engineer );; 27y  "

# Extract the name by removing the prefix "968-" and the suffix containing role and age information, then stripping any leading/trailing spaces. Also, convert to lowercase.
name = raw_data.lower().removeprefix("968-").strip("( d,( D@t@ Engineer );; 27y  ")
# Extract the role by removing the prefix and suffix, then replacing "@" with "a". Convert to lowercase.
role = raw_data.lower().removeprefix("968-maria,( ").removesuffix(" );; 27y  ").replace("@","a")
# Extract the age by slicing the raw data string.
age = raw_data[30:32]

print(f"name : {name} | role : {role} | age : {age}")
```



# This is my first Python script, written as part of my coding journey!
# I wrote and debugged it myself without referencing outside sources, just using my own reasoning.

# The following block is commented out. It demonstrates how to check for spaces in a string.
"""
text = "Accounting"
print(len(text))              # Prints the length of the string including spaces
print(len(text.strip()))      # Prints the length after removing leading/trailing spaces

nm_of_space = len(text) - len(text.strip())    # Calculates the number of leading/trailing spaces
is_data_clean = len(text) == len(text.strip()) # Checks if there are no leading/trailing spaces
print(f"Nm of Spaces is {nm_of_space}")        # Outputs number of spaces
print(f"Is data clean : {is_data_clean}")      # Outputs if data is clean or not
"""

# Here is the raw data string I want to parse for name, role, and age.
raw_data = "968-Maria,( D@t@ Engineer );; 27y  "

# Extract the name by:
# - Converting to lowercase, removing the "968-" prefix, and stripping unwanted characters from start and end.
name = raw_data.lower().lstrip("968-").strip("( d,( D@t@ Engineer );; 27y  ")

# Extract the role by:
# - Converting to lowercase, removing the "968-maria,( " prefix, stripping unwanted characters from the end,
# - and replacing '@' with 'a' for a cleaner role name.
role = raw_data.lower().lstrip("968-maria,( ").rstrip(" );; 27y  ").replace("@","a")

# Extract the age by slicing the string at specific indices (found by counting characters).
age = raw_data[30:32]

# Output the results in a readable format.
print(f"name : {name} | role : {role} | age : {age}")

