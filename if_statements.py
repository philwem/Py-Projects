# Validate the Quality and Correctness of Email Values

email = 'Philip@@gmail.com'
# clean  the string
email = email.strip()

# - Must not be empty
if email == "" :
    print("Enter email !!!!!!!")
# - Must contain '.' and '@'
elif   not ('.'  in email and '@' in email) :
    print("Email must contain '.' and '@")
# - Must contain exactly one '@' symbol
elif email.count("@") != 1:
    print("Email must contain exactly one '@' symbol")  
# - Must end with '.com', '.org', or '.net'
elif  not email.endswith(('.com', '.org', '.net')):
    print("Email must end with '.com', '.org', or '.net")       
# - Must not be longer than 254 characters
elif  len(email) > 254:
    print("Email must end with '.com', '.org', or '.net")  
# - Must start and end with a letter or digit
elif  not(email[0].isalnum() and email[-1].isalnum()):
    print("Email not start and end with a letter or digit")
else: 
    print("Email is valid")
