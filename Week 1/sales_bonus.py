"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

LOW_BONUS_RATE = 0.1  # 10% bonus rate for sales which are under $1000
HIGH_BONUS_RATE = 0.15  # 15% bonus rate for sales which are $1,000 or over
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * LOW_BONUS_RATE
    else:
        bonus = sales * HIGH_BONUS_RATE
    print(int(bonus))
    sales = float(input("Enter sales: $"))

