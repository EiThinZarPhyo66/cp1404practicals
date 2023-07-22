MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    choice = input("Choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = validate_score()
        elif choice == "P":
            determine_score(score)
        elif choice == "S":
            display_stars(score)
        else:
            print("Invalid score")
        print(MENU)
        choice = input("Choice: ").upper()
    print("farewell")


def display_stars(score):
    """Display stars"""
    for i in range(score):
        print("*", end='')
    print()


def determine_score(score):
    """Determine result based on score"""
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    print(result)


def validate_score():
    """Get the valid score"""
    score = int(input("Score: "))
    if score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


main()