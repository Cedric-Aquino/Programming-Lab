# --- Collections ---
# List
my_list = ["Cedric", 18, True]

# Tuple
my_tuple = ("Python", 100, False)

# Set
my_set = {"Code", 1, True}

# Dictionary
my_dict = {
    "name": "Cedric",
    "age": 18,
    "is_student": True
}

# --- Condition (if statement returning True/False) ---
age = my_dict["age"]

result = age >= 18  # condition

# --- Output ---
print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)

print("\nIs age 18 or above?", result)

# Optional if statement usage
if result:
    print("You are an adult.")
else:
    print("You are not an adult.") 