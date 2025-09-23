# students = ["Hermione","Harry", "Ron"]

# while len(students) < 10: 
#     students.append(input("gimme your name: "))

#     for i in range(len(students)):
#         print(i+ 1, students[i])

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"

}
for student in (students):
    print(student, students[student], sep=", ")

