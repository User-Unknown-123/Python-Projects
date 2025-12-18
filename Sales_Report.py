import csv


# q1 create sales.txt and write data
def create_txt():
    f = open("sales.txt", "w")
    n = int(input("How many sales records: "))

    for i in range(n):
        bill = input("Enter bill no: ")
        item = input("Enter item name: ")
        amount = input("Enter amount: ")
        f.write(bill + "," + item + "," + amount + "\n")

    f.close()
    print("sales.txt created")


# q2 append new sales data
def append_txt():
    f = open("sales.txt", "a")
    bill = input("Enter bill no: ")
    item = input("Enter item name: ")
    amount = input("Enter amount: ")
    f.write(bill + "," + item + "," + amount + "\n")
    f.close()
    print("New sales record added")


# q3 convert txt to csv
def convert_to_csv():
    txt = open("sales.txt", "r")
    csvf = open("sales.csv", "w", newline="")
    writer = csv.writer(csvf)

    writer.writerow(["BillNo", "Item", "Amount"])

    for line in txt:
        data = line.strip().split(",")
        writer.writerow(data)

    txt.close()
    csvf.close()
    print("Converted to sales.csv")


# q4 read and display csv file
def read_csv():
    f = open("sales.csv", "r")
    reader = csv.reader(f)

    print("Sales Records:")
    for row in reader:
        print(row)

    f.close()


# q5 calculate total sales amount
def total_sales():
    f = open("sales.csv", "r")
    reader = csv.reader(f)

    total = 0
    next(reader)  # skip heading

    for row in reader:
        total += int(row[2])

    f.close()
    print("Total sales amount:", total)


# menu driven program
while True:
    print("\nMenu")
    print("1. Create sales.txt")
    print("2. Add new sales data")
    print("3. Convert sales.txt to sales.csv")
    print("4. Read sales.csv")
    print("5. Calculate total sales")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        create_txt()
    elif ch == 2:
        append_txt()
    elif ch == 3:
        convert_to_csv()
    elif ch == 4:
        read_csv()
    elif ch == 5:
        total_sales()
    elif ch == 6:
        print("Exit")
        break
    else:
        print("Invalid choice")