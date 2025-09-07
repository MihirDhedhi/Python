import sqlite3
conn = sqlite3.connect('student_enrollment.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS enrollments')
cursor.execute('DROP TABLE IF EXISTS students')
cursor.execute('DROP TABLE IF EXISTS subjects')
cursor.execute('''CREATE TABLE students (
    Enrollment INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)''')
cursor.execute('''CREATE TABLE subjects (
    SubjectId INTEGER PRIMARY KEY AUTOINCREMENT,
    SubjectName TEXT NOT NULL
)''')
cursor.execute('''CREATE TABLE enrollments (
    EnrollmentId INTEGER PRIMARY KEY AUTOINCREMENT,
    Enrollment INTEGER,
    SubjectId INTEGER,
    Mark INTEGER,
    FOREIGN KEY(Enrollment) REFERENCES students(Enrollment),
    FOREIGN KEY(SubjectId) REFERENCES subjects(SubjectId)
)''')
conn.commit()
print("Database tables created successfully.")
students_data = [
    (92400133015, 'mihir'),
    (92400133170, 'nemil')
]
subjects_data = [
    ('PWP',),
    ('DS',),
    ('OOP',)
]
cursor.executemany("INSERT INTO students VALUES (?, ?)", students_data)
cursor.executemany("INSERT INTO subjects (SubjectName) VALUES (?)", subjects_data)
conn.commit()
print("Student and subject data inserted.")
cursor.execute("SELECT SubjectId FROM subjects WHERE SubjectName = 'PWP'")
pwp_id = cursor.fetchone()[0]
cursor.execute("SELECT SubjectId FROM subjects WHERE SubjectName = 'DS'")
ds_id = cursor.fetchone()[0]
cursor.execute("SELECT SubjectId FROM subjects WHERE SubjectName = 'OOP'")
oop_id = cursor.fetchone()[0]
enrollment_data = [
    (92400133015, pwp_id, 95),
    (92400133015, ds_id, 88),
    (92400133170, pwp_id, 85),
    (92400133170, oop_id, 92)
]
cursor.executemany("INSERT INTO enrollments (Enrollment, SubjectId, Mark) VALUES (?, ?, ?)", enrollment_data)
conn.commit()
print("Students enrolled in multiple subjects.")
cursor.execute('''SELECT s.name, sub.SubjectName, e.Mark
                  FROM enrollments e
                  JOIN students s ON e.Enrollment = s.Enrollment
                  JOIN subjects sub ON e.SubjectId = sub.SubjectId
                  WHERE s.name = 'mihir'
                  ORDER BY sub.SubjectName''')
mihir_records = cursor.fetchall()
print("\nmihir's Records:")
for record in mihir_records:
    print(f"Name: {record[0]}, Subject: {record[1]}, Mark: {record[2]}")
conn.close()