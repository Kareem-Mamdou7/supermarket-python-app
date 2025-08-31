items = [
    {"name": "apple", "price": 0.60, "quantity": 20},
    {"name": "banana", "price": 0.40, "quantity": 15},
    {"name": "orange", "price": 0.30, "quantity": 30},
    {"name": "watermelon", "price": 2.50, "quantity": 5},
]

# column widths
name_w = 15
price_w = 10
qty_w = 10

# headers
print(f"{'Name':<{name_w}}{'Price':>{price_w}}{'Quantity':>{qty_w}}")
print("-" * (name_w + price_w + qty_w))

# rows
for item in items:
    print(
        f"{item['name']:<{name_w}}{item['price']:>{price_w}.2f}{item['quantity']:>{qty_w}}"
    )

hi = 10000
hello = 100
hola = 1
print(f"{hi:>35}")
print(f"{hello:>35}")
print(f"{hola:>35}")
