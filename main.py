
items = input("what would you like to buy?: ")
price = float(input("ok, the price for the item is?: "))
quantity = int(input("how many would you like to buy?: "))

total = price * quantity
print(f"you have bought {quantity} x {items}/s")
print(f"your total is ${total}")