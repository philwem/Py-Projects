user_name =""
password ="mama12389"
email = "phil@gmail.com"
age = 23

#Check if a user's name is not empty and the age is greater than or equal to 18
print(bool(user_name) and age >= 18)  # name not empty & age >= 18


#Check if the password is at least 8 characters long and does not contain spaces
print(len(password) >= 8 and " " not in password)  # password valid

#Check if a user's email is not empty, contains '@', and ends with '.com'
print(email and "@" in email and email.endswith(".com"))  # email valid

#Check if a username is a string, is not None, and is longer than 5 characters
print(isinstance(user_name, str) and len(user_name) > 5)  # username valid

#Check if the user is either an admin or a moderator,
#and either they're not banned or they've verified their email
# Role check
role, is_banned, email_verified = "admin", False, True
print((role in {"admin", "moderator"}) and (not is_banned or email_verified))


