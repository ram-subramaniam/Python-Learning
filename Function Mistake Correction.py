price_input = float(input("Enter value for price \n"))
cost_input = float(input("Enter value for cost \n"))
discount_input = float(input("Enter value for discount \n"))


def calculate_profit_exam(price, discount, cost):
    profit = price - cost
    discount_percent = 1-discount/100
    discounted_price = (price * discount_percent)
    profit_with_discount = discounted_price-cost
    print(f"Price is = {price_input}")
    print(f"Cost is = {cost_input}")
    print(f"Discount is = {discount_input}")
    print(f"Discounted Price is = {discounted_price}")
    print(f"Profit without discount is = {profit}")
    print(f"Profit with discount is = {profit_with_discount}")
    # print("${:.2f}".format(amt2))
    print("Profit with discount ${:.2f}".format(profit_with_discount))


calculate_profit_exam(price_input, discount_input, cost_input)
