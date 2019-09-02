def r():
  price_book = 24.95
  percentage = 40
  qty_books = 60
  qty_first_book = 1
  first_book = 3
  rest_batch = ((qty_books-qty_first_book)*0.75)
  price_batch = (price_book/100) * percentage
  print(price_batch + first_book + rest_batch, 'euro')

r()