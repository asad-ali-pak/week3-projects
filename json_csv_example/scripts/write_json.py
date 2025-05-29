import json

product = {
    "id": 101,
    "name": "Laptop",
    "price": 65000,
    "in_stock": True
}

with open("../data/product.json", "w") as f:
    json.dump(product, f, indent=4)
