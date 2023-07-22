import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    score = random_score
    print(f"Random score is {score}.")
    result = determine_result(score)
    print(result)


def determine_result(score):
    """Determine result based on score"""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
