# menu for student file

def create_file():
    f = open("students.txt", "w")
    n = int(input("How many students: "))

    for i in range(n):
        name = input("Enter name: ")
        roll = input("Enter roll: ")
        f.write(name + "," + roll + "\n")

    f.close()
    print("File created")


def read_file():
    f = open("students.txt", "r")
    print("Student Records:")
    print(f.read())
    f.close()


def append_file():
    f = open("students.txt", "a")
    name = input("Enter name: ")
    roll = input("Enter roll: ")
    f.write(name + "," + roll + "\n")
    f.close()
    print("Record added")


def count_lines():
    f = open("students.txt", "r")
    count = 0
    for line in f:
        count += 1
    f.close()
    print("Total students:", count)


def search_student():
    name = input("Enter name to search: ")
    f = open("students.txt", "r")
    found = False

    for line in f:
        if name in line:
            print("Student found:", line)
            found = True

    if not found:
        print("Student not found")

    f.close()


while True:
    print("\nMenu")
    print("1. Create file and write data")
    print("2. Read file")
    print("3. Add new student")
    print("4. Count students")
    print("5. Search student")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        create_file()
    elif ch == 2:
        read_file()
    elif ch == 3:
        append_file()
    elif ch == 4:
        count_lines()
    elif ch == 5:
        search_student()
    elif ch == 6:
        print("Exit")
        break
    else:
        print("Invalid choice")