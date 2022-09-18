

def profit_calc(discount, cost, price):

    net_price = float ((1 - (discount_input / 100)) * price)
    profit = (net_price - cost)
    print(f"Price is {price}")
    print(f"Discount is {discount}")
    print(f"Net Price is {net_price}")
    print(f"Cost is {cost}")
    print(f"Net Profit is {profit}")

net_discount = int(discount_input)
net_price = int(price_input)
net_cost = int(cost_input)

if int(discount_input) < 0:
    print("Can be less than 0% discount")
elif int(discount_input) > 0:
    net_discount = int(discount_input)
elif int(price_input) > 0 :



profit_calc(net_discount, net_cost, net_price)


