MINIMUM_LENGTH = 6


def main():
    password = get_password()
    while len(password) < MINIMUM_LENGTH:
        print("Password is too short. Minimum length is", MINIMUM_LENGTH)
        password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Display asterisks as much as user's password"""
    print("*" * len(password))


def get_password():
    """Get password from users."""
    password = input("Enter a password: ")
    return password


main()
