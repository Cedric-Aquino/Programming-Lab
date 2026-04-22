# Activity 1: Access Elements
colors = ("red", "green", "blue")
print(colors[0])
print(colors[-1])

# Activity 2: Slicing
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])

# Activity 3: Tuple Methods
nums = (1, 2, 2, 3, 2)
print(nums.count(2))
print(nums.index(3))

# Activity 4: Tuple Packing & Unpacking
point = (5, 10)
(x, y)=point
print("x =", x)
print("y =", y)

# Activity 5 (Challenge): Combine Tuples
t1 = (1, 2)
t2 = (3, 4)
t3=(t1+t2)*2
print(t3)