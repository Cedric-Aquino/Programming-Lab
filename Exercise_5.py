# A program for you to calculate the length of a string.
a="Exercise"
print("length:", len(a))

#  A program counts the number of characters in a string.
b="Exercise"
count=len(b)
print("\n""number of characters:", count)

#  A program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
text=("exercise")
first=text[0]
new_text=first + text[1:].replace(first, '$')
print("\n""Result:", new_text)

#  A program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
a=("Exercise")
b=("Program")
new_a = b[:2] + a[2:]
new_b = a[:2] + b[2:]
print("\n""Result:", new_a + " " + new_b)

# Using + Concatenate Strings in Python using 4 variables concatenate them with spaces
a="I"
b="am"
c="learning"
d="Python"
print("\n" + a + " " + b + " " + c + " " + d)


# Using + Concatenate Strings in Python get two strings from user input and concatenate them
a=input("\nEnter first string: ")
b=input("Enter second string: ")
print("Concatenated:", a + " " + b)


# Using + Concatenate in Python using your name and your age in a paragraph
name = input("\nEnter your name: ")
age = input("Enter your age: ")
print("My name is " + name + " and I am " + age + " years old.")