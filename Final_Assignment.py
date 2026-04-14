# LIST
my_list = ["apple", "banana", "cherry"]
my_list.append("orange")
my_list.remove("banana")
my_list.sort()

print("List:", my_list)


# TUPLE
my_tuple = (1, 2, 3)

try:
    my_tuple[0] = 10
except TypeError as e:
    print("Tuple Error:", e)
    print("Explanation: Tuples are immutable (cannot be changed).")


# SET
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)

print("Set:", my_set)


# DICTIONARY
my_dict = {"name": "Cedric", "age": 18}
my_dict["grade"] = "10"
my_dict["age"] = 19

print("Dictionary Keys:", my_dict.keys())