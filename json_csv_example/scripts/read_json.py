import json

with open("/home/asad/pyfile/python/week3-projects/json_csv_example/data/product.json", "r") as f:
    product = json.load(f)
    print(product)
