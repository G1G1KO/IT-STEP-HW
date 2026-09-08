import mysql.connector

db_connector = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "University"
)

db_cursor = db_connector.cursor()

# ========== მონაცემთა ბაზის შექმნა ==========

db_cursor.execute("CREATE DATABASE University;")


# ========== ცხრილის შედგენა ==========


create_table_query = """
CREATE TABLE IF NOT EXISTS Students(
    studentID INT PRIMARY KEY AUTO_INCREMENT,
    studentLastName VARCHAR(20) NOT NULL,
    studentFirstName VARCHAR(20) NOT NULL,
    studentAge INT NOT NULL
);"""

db_cursor.execute(create_table_query)


# ========== მონაცემების შეტანა ==========


students = [
    ["აბულაძე","გრიგოლ", 31],
    ["გერგაული", "ანა", 25],
    ["კახიძე", "ქეთევან", 26],
    ["შალიკაშვილი", "ანდრო", 29],
    ["ხარაზაშვილი", "ნინო", 24]
]

insert_book_query = "INSERT INTO Students (studentLastName, studentFirstName, studentAge) VALUES (%s, %s, %s)"

for student in students:
    db_cursor.execute(insert_book_query, (student[0], student[1], student[2]))


db_connector.commit()


# ========== ახალი სტუდენტის დამატება ===========


new_student = ["კახიძე", "კოტე", 27]


insert_query = "INSERT INTO Students (studentLastName, studentFirstName, studentAge) VALUES (%s, %s, %s)"


db_cursor.execute(insert_query, new_student)

db_connector.commit()


# ========== დავალაგოთ მონაცემები ანბანის მიხედვით (გვარი, სახელი) ==========

sort_data_query = """
SELECT * FROM Students
ORDER BY studentLastName ASC, studentFirstName ASC;
"""

db_cursor.execute(sort_data_query)

sorted_students = db_cursor.fetchall()
for student in sorted_students:
    print(student)