book_price = 24.95
discount = book_price * .4
discount_price = book_price - discount
shipping_cost_first = 3
shipping_cost_rem = 0.75
total_cost = discount_price * 60 + shipping_cost_first + shipping_cost_rem * 59
print (total_cost)