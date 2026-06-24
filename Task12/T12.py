
import csv

filename = "Task1/info.csv"


''' 1)
def add_student():
    print("--- Enter New Student's Info ---")
    student_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")
    subject_name = input("Enter Subject Name: ")
    mark = int(input("Enter Mark: "))

    new_student = [student_id, name, age, grade, subject_name, mark]

    all_rows = []


    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)  
        
        for row in reader:
            row[0] = int(row[0]) 
            all_rows.append(row)

    for existing_student in all_rows:
        if existing_student[0] == student_id:
            print(f"\nError: Student With ID: {student_id} Exists!")
            return
        

    all_rows.append(new_student)

    all_rows.sort(key=lambda x: x[0])

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(all_rows)

    print(f"\nStudent {name} added successfullyz")

add_student()
'''





''' 2)
def print_info():

    print("--- Menu ---")
    print("1. Print All Students")
    print("2. Search For Student")
    choice = input("Choose (1 or 2): ")

    with open(filename, mode = "r", encoding="utf-8") as file:
        reader =  csv.reader(file)
        header = next(reader)


        if choice == "1":
            print("--- All Students ---")
            print(f"{header[0]:<5} {header[1]:<12} {header[2]:<5} {header[3]:<7} {header[4]:<15} {header[5]:<5}")
            print("-" * 55)
            for row in reader:
                print(f"{row[0]:<5} {row[1]:<12} {row[2]:<5} {row[3]:<7} {row[4]:<15} {row[5]:<5}")


        elif choice == "2":
            search_id = int(input("Enter Student's ID: "))
            student_found = False


            for row in reader:
                if int(row[0]) == search_id:
                    print("\n--- Found Student Info ---")
                    print(f"Name: {row[1]}")
                    print(f"Age: {row[2]}")
                    print(f"Grade: {row[3]}")
                    print(f"Subject: {row[4]}")
                    print(f"Mark: {row[5]}")
                    student_found = True
                    break 

            if not student_found:
                    print(f"\nStudent With ID {search_id} Was Not Found!")
            
        else:
            print("\nWrong Choice! Only Enter 1 or 2.")


print_info()
'''


''' 3)
def average_by_subject():
    subject_marks = {}

    with open(filename, mode = "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            subject = row[4]
            mark = int(row[5])

            if subject not in subject_marks:
                subject_marks[subject] = []

            subject_marks[subject].append(mark)


    print("\n--- Average Grade By Subject ---")

    for subject, marks in subject_marks.items():
        average = sum(marks) / len(marks)
        
        print(f"Subhect: {subject:<15} | Average: {average:.2f}")


average_by_subject()
'''



''' 4)
def update_info():

    print("--- Student Mark Update ---")
    search_id = int(input("Enter Student's ID: "))
    search_subject = input("Enter Subject's Name: ")
    new_mark = int(input("Enter New Grade: "))

    all_rows = []
    student_found = False

    with open(filename, mode = "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:

            if int(row[0]) == search_id and row[4] == search_subject:
                row[5] = new_mark
                student_found = True

            all_rows.append(row)

    if not student_found:
        print(f"Student with ID {search_id} And Subject {search_subject} Was Not Found!")
        return
    
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(all_rows)

    print("Updated Successfully")


update_info()
'''







''' 5)
students = [
  {'id': 8, 'name': 'Nika', 'age': 19, 'grade': 'B', 'subject_name': 'Physic', 'mark': 87},
  {'id': 19, 'name': 'Nuca', 'age': 18, 'grade': 'B', 'subject_name': 'Mathematic', 'mark': 84},
  {'id': 11, 'name': 'Archil', 'age': 21, 'grade': 'C', 'subject_name': 'Mathematic', 'mark': 74},
  {'id': 25, 'name': 'Nino', 'age': 20, 'grade': 'A', 'subject_name': 'Informatic', 'mark': 95},
  {'id': 22, 'name': 'Giga', 'age': 20, 'grade': 'A', 'subject_name': 'Biology', 'mark': 81},
  {'id': 31, 'name': 'Lana', 'age': 22, 'grade': 'B', 'subject_name': 'Geography', 'mark': 88},
  {'id': 3, 'name': 'Nino', 'age': 23, 'grade': 'B', 'subject_name': 'Informatic', 'mark': 85},
]


new_student = {
  'id': 5,
  'name': 'Demetre',
  'age': 18,
  'grade': 'A',
  'subject_name': 'Informatic',
  'mark': 94
}



def add_students(student_list, new_student):

    student_list.append(new_student)

    student_list.sort(key = lambda x: x['id'])

    fieldnames = ['id', 'name', 'age', 'grade', 'subject_name', 'mark']

    with open(filename, mode="w", newline="",encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(student_list)

    print("Successfully Added new Student")


add_students(students, new_student)
'''