import json

file_path = "./Supermarket System OOP/products.json"

with open(file_path, "r") as f:
    products = json.load(f)

print(products)
new_product = {
    "name": "pomegrenate",
    "price": 15.00,
    "quantity": 10,
}
products.append(new_product)

with open(file_path, "w") as file:
    json.dump(products, file, indent=2)
