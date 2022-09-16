

def profit_calc(discount, cost, price):

    net_price = (1-(discount/100))*price
    print(f"Net Price is {net_price}")
    profit = (net_price-cost)
    print(f"Net Profit is {profit}")


discount_input = input("pls enter discount value\n")
if float(discount_input) < 0:
    print("Can be less than 0% discount")
elif float(discount_input) > 0:
    net_discount = float(discount_input)

price_input = input("pls enter price value\n")
net_price = int(price_input)

cost_input = input("pls enter cost value\n")
net_cost = int(cost_input)

profit_calc(net_discount, net_cost, net_price)


