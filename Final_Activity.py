# PART 1: Identify & Create

# Tuple
fruits = ("apple", "banana", "mango", "grapes", "orange")

# List
tasks = ["wake up", "eat breakfast", "study", "exercise", "sleep"]

# Set
numbers = {1, 2, 3, 4, 5}

# Dictionary
student = {
    "name": "Cedric",
    "age": 18,
    "course": "IT"
}


# PART 2: Manipulation Challenge

# List Tasks
tasks.append("do homework")   # Add
tasks.remove("exercise")      # Remove
tasks.sort()                  # Sort

# Tuple Task (will cause error if uncommented)
# fruits[0] = "pineapple"

# Set Tasks
numbers.add(6)                # Add
numbers.remove(2)             # Remove

duplicate_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(duplicate_list)  # Remove duplicates

# Dictionary Tasks
student["grade"] = "A"        # Add new key
student["age"] = 19           # Update value


# OUTPUT
print("Fruits (Tuple):", fruits)
print("Tasks (List):", tasks)
print("Numbers (Set):", numbers)
print("Unique Numbers from List:", unique_numbers)

print("Student Dictionary:", student)
print("Keys:", student.keys())
print("Values:", student.values())


# Explanation for tuple
print("\nTuple Explanation: Tuples cannot be changed (immutable), so modifying them causes an error.")