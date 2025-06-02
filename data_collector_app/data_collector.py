import csv
import os

file_name = "user.csv"

# Create CSV file with headers if it doesn't exist
if not os.path.exists(file_name):
    with open(file_name, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Age", "Email"])

# Collect user data
print("Enter user information:")
name = input("Name: ")
age = input("Age: ")
email = input("Email: ")

# Save user data to CSV
with open(file_name, "a", newline='') as f:
    writer = csv.writer(f)
    writer.writerow([name, age, email])

print("\n User added successfully!")

# Prepare summary
summary = {
    'total': 0,
    'avg_age': 0,
    'users': []
}

# Read data and calculate summary
with open(file_name, "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    users = list(reader)

    summary['users'] = users
    summary['total'] = len(users)
    
    # Extract and average valid ages
    ages = [int(user[1]) for user in users if user[1].isdigit()]
    summary['avg_age'] = sum(ages) / len(ages) if ages else 0

# Show summary
print("\n User Summary")
print(f"Total Users: {summary['total']}")
print(f"Average Age: {summary['avg_age']:.2f}")
print("Names:")
for user in summary['users']:
    print(f"- {user[0]}")
