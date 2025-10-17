# 3 attempts
# Yes within three attempts -> "Glad we are on the same page!"
# Otherwise "3 strikes. You're out!"

attempts = 0
while attempts < 3:
    answer = input("do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we are on the same page!")
        break
    attempts += 1
else :
    print("3 strikes. You're out!")