
import csv

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    subjects = ['Math', 'Science', 'English']
    marks = []

    for subject in subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / len(subjects)

    with open('students.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, roll] + marks + [total, f"{percentage:.2f}%"])
    print("Student record added successfully!\n")

def view_students():
    try:
        with open('students.csv', 'r') as f:
            reader = csv.reader(f)
            print("\n--- Student Records ---")
            print("Name | Roll | Math | Science | English | Total | Percentage")
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("No records found. Please add students first.\n")

def menu():
    while True:
        print("\n--- Student Marks Management ---")
        print("1. Add Student Record")
        print("2. View All Records")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()
