# List Example
students = ["Hermione", "Harry", "Ron"]

print(students[0])  # Hermione
print(students[1])  # Harry
print(students[2])  # Ron

print("\n#################\n")

for student in students:
    print(student)  # Hermione, Harry, Ron

print("\n#################\n")

for i in range(len(students)):
    print(i+ 1, students[i])  # Hermione, Harry, Ron


print("\n#################\n")

# Dictionary Example
students1 = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student1 in students1:
    print(f"{student1} is in {students1[student]}")  # Hermione, Harry, Ron

print("\n#################\n")

# List of Dictionaries Example
students2 = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

print(f"Name\t\t\tHouse\t\t\tPatronus")
for student2 in students2:
    print(f"{student2["name"]}\t\t\t{student2["house"]}\t\t{student2["patronus"]}")