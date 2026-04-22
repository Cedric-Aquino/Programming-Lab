# Activity 1: Remove Duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
x=set(numbers)
print(x)

# Activity 2: Add and Remove
fruits = {"apple", "banana"}    
fruits.add("orange")
fruits.remove("banana")
print(fruits)

# Activity 3: Set Operations
A = {1, 2, 3}
B = {3, 4, 5}

c=A.union(B)
print(c)
C=A.intersection(B)
print(C)

# Activity 4 (Challenge): Common Students
classA = {"John", "Ana", "Mark"}
classB = {"Ana", "Mark", "Liza"}

classC=classA.intersection(classB)
print(classC)
classC=classA.union(classB)
print(classC)