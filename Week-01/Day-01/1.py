stock_prices=[int(a) for a in input().split(",")]

if len(stock_prices) < 2:
        raise ValueError('Requires at least 2 price values')

min_price  = stock_prices[0]
max_profit = stock_prices[1] - stock_prices[0]
for current_time in range(1, len(stock_prices)):
    current_price = stock_prices[current_time]
    potential_profit = current_price - min_price
    max_profit = max(max_profit, potential_profit)
    min_price  = min(min_price, current_price)

print(max_profit)