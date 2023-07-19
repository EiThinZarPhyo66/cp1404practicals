DISCOUNT_RATE = 0.1  # 10% discount rate is applied for the total price which is over $100
DISCOUNT_THRESHOLD = 100
total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item
if total_price > DISCOUNT_THRESHOLD:
    discount_price = total_price * DISCOUNT_RATE
    total_price -= discount_price
else:
    total_price = total_price
print(f"Total price for {number_of_items} items is ${total_price:.2f}")


