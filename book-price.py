book_price = 24.95
discount_price = book_price * .6
book_count = float (input('Number of copies purchased'))
total_cost = discount_price * book_count
shipping_cost = 3 + (.75 * (book_count -1))
total = total_cost + shipping_cost
print (total_cost)