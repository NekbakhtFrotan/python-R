stock = {"pen": 25, "notebook": 12, "marker": 8}
delivery = {"notebook": 10, "marker": 5, "eraser": 20}

total_items = 0
for item, delivered_qty in delivery.items():
    if item in stock:
        stock[item] += delivered_qty
    else:
        stock[item] = delivered_qty

for item in sorted(stock):
    print(f"{item}: {stock[item]}")
    total_items += stock[item]

print(f"Total items in stock: {total_items}")
