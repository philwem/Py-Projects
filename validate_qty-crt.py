# Validate the Quality and Correctness of Password
password = "BILLHEYAc    "
email = "BILLYAAcH"
# clean the string 
# password = password.strip()
email = email.strip()
# - Must not be empty
if password == "":
    print("Enter password")
# - Must be at least 8 characters
elif  not  len(password) >= 8 :
    print("Password must be at least 8 character")   
# - Must include at least 1 uppercase
elif   not any(c.isupper() for c in password):
    print("Password must include at least 1 uppercase")       
# - Must include at least 1 lowercase
elif   not any(c.islower() for c in password):
    print("Password must include at least 1 lowercase")   
# - Must not be same as the email
elif password == email :
    print("Password must  not be same as the email")   
# - Must not contain any spaces
elif not password == password.strip() :
    print("Password must not contain any spaces")   
# - Must start and end with a letter or digit
elif not(password[0].isalnum() and password[-1].isalnum() ) :
    print("Password must start and end with a letter or digit")   
else :
    print ("Password valid")