# Activity 1: Fill in the Blanks
student = {
   "name": "Ana",
   "age": 20,
   "course": "IT"
}
print(student["name"])

# Activity 2: Add and Update
student = {"name": "Ana", "age": 20}
student.update({"grade": 95})
student["age"]=21
print(student)

# Activity 3: Loop Through Dictionary
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
for x, y in car.items():
    print(x, ":", y)

# Activity 4 (Challenge): Mini Phonebook
numbers={
    "Charlz": 9939025809,
    "Jirus": 9519526826,
    "jerone": 9389386772,
    "jeshley": 9925583351
}
name=input("Enter name: ")
print(numbers[name])