import csv
from datetime import datetime

FILENAME = 'expenses.csv'

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ") or str(datetime.today().date())
    category = input("Category: ")
    amount = float(input("Amount: "))
    note = input("Note: ")

    with open(FILENAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, note])
    print("✅ Expense added.")

def view_expenses():
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = 0
    with open(FILENAME, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0].startswith(month):
                total += float(row[2])
    print(f"💰 Total spent in {month}: ₹{total}")

def menu():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Exit")
        choice = input("Choose: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            monthly_summary()
        elif choice == '4':
            break

menu()
