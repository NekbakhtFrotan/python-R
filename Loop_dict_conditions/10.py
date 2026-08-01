prices = {"rice": 75.0, "oil": 185.0, "milk": 95.0, "eggs": 12.0}
quantities = {"rice": 20, "oil": 10, "milk": 15, "eggs": 60}

total_value = 0.0
max_product = None
max_value = 0.0

for product, price in prices.items():
    quantity = quantities.get(product, 0)
    stock_value = price * quantity
    print(f"{product}: {stock_value}")
    total_value += stock_value
    if max_product is None or stock_value > max_value:
        max_product = product
        max_value = stock_value

print(f"Total inventory value: {total_value}")
print(f"Highest-value stock: {max_product}")
