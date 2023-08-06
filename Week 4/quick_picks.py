import random
MIN_VALUE = 1
MAX_VALUE = 45
NUMBERS_PER_LINE = 6


def main():
    """Generate random numbers between MIN_VALUE AND MAX_VALUE with NUMBERS_PER_LINE """
    number_of_quick_picks = get_input()
    for i in range(number_of_quick_picks):
        quick_picks = generate_quick_picks()
        display_quick_picks(quick_picks)


def get_input():
    """Get the user's input of number of quick picks."""
    number_of_quick_picks = int(input("How many quick picks? "))
    return number_of_quick_picks


def generate_quick_picks():
    """Generate quick picks and sort them"""
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        random_number = random.randint(MIN_VALUE, MAX_VALUE)
        if random_number not in numbers:
            numbers.append(random_number)
        numbers.sort()
    return numbers


def display_quick_picks(numbers):
    """Display quick picks nicely."""
    for number in numbers:
        print("{:2d}".format(number), end=" ")
    print()


main()