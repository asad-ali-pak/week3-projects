import csv

data = [
['name','class','marks'],
['Ali',10,85],
['Ammar',9,78],
['umar',10,90],
['usman',9,78]
]

with open ("/home/asad/pyfile/python/week3-projects/json_csv_example/data/student.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data)
    writer.writerow([['Abubakar',10,95]])
    print(data)