def calculate_profit_exam(price, discount, cost):
    profit = price - cost
    discount_percent = 1 - discount / 100
    discounted_price = (price * discount_percent)-cost
    dollar_discount = (price - discounted_price)
    profit_with_discount = price - discounted_price

    print("Price is ${:.2f}".format(price))
    print("Cost is ${:.2f}".format(cost))

    print(f"Discount is = {discount}%")
    print("Profit without discount is ${:.2f}".format(profit))
    print("Profit with discount is ${:.2f}".format(dollar_discount))
    print("Discount Price is ${:.2f}".format(discounted_price))
    print("Profit with discount ${:.2f}".format(profit_with_discount))


price = float(input("Enter value for price \n"))
cost = float(input("Enter value for cost \n"))
discount = float(input("Enter value for discount \n"))

calculate_profit_exam(price, discount, cost)
