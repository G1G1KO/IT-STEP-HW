#Task 6

myDict = {
  "students": [
    {"id": 20, "name": "Giorgi", "age": 25},
    {"id": 25, "name": "Giorgi", "age": 23},
    {"id": 56, "name": "Nika", "age": 25},
    {"id": 100, "name": "Nika", "age": 22},
    {"id": 1232, "name": "Dato", "age": 22},
    {"id": 846723, "name": "Archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "56": "B", "100": "A", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "56": "B", "100": "A", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "56": "A", "100": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
  ]
}





print("\nStudent ID's: ", end= '')
idArray = []
for student in myDict['students']:
    print(student['id'], end=' ')
    idArray.append(student['id'])

while True:
    idChoice = int(input("\nChoose Student ID (0 to quit): "))
        
    if idChoice == 0:
        print("\nEnded Successfully")
        break

    if idChoice not in idArray:
        print("Wrong ID, Try Again")
        continue

    print("\n====== Student Information ======")
    for student in myDict['students']:
        if student['id'] == idChoice:
            print(f"ID: {idChoice}, Name: {student['name']}, Age: {student['age']}")
            break 

    for subject in myDict['subjects']:
        grade = subject['grades'].get(str(idChoice))
        print(f"Subject: {subject['name']}, Grade: {grade}")