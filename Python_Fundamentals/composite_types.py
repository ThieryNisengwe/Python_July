
# Araay [item, item, item,] - : Python - lists
grades = [9.8, 8.7, 7.6]

print(grades)
print(len(grades))

grades.append(10.0)
print(grades)

grades_copy = grades[:]

print(grades_copy, grades)

# Objects in JS are Dictionaries in Python

student = {
  "first_name" : "Thiery",
  "last_name" : "Nis",
  "age" : 20,
  "grade" : 9.6,
  "stack" : "Python/Flask",
  "passed" : True
}

print(student["first_name"])
l_n = "last_name"
print(student[l_n])

student["instructor"] = "Alfredo Salazar"
print(student)

course = ("Python", "4 weeks", "Spencer Rauch")
print(course)