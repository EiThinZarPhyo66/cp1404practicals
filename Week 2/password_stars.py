MINIMUM_LENGTH = 6


def main():
    password = get_password()
    print("*" * len(password))


def get_password():
    """Get the password from the user"""
    password = input("Enter a password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short. Minimum length is", MINIMUM_LENGTH)
        password = input("Enter a password: ")
    return password


main()
