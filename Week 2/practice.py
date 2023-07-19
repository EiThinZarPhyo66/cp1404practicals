MINIMUM_LENGTH = 6
password = input("Enter a password: ")

while len(password) < MINIMUM_LENGTH:
    print("Password is too short. Minimum length is", MINIMUM_LENGTH)
    password = input("Enter a password: ")
print("*" * len(password))
