# input list
lst = [1, 2, 3, 2, 4, 1, 5, 6]

# q1 remove duplicates
new_list = []

for i in lst:
    if i not in new_list:
        new_list.append(i)

print("No duplicates:", new_list)

print()

# q2 even numbers using list comprehension
even_list = [i for i in lst if i % 2 == 0]
print("Even numbers:", even_list)

print()

# q3 second largest element
unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

unique.sort()
print("Second largest:", unique[-2])

print()

# q4 sum of inner lists
nested = [[1, 2], [3, 4, 5], [6]]

for i in nested:
    print("Sum:", sum(i))

print()

# q5 shallow and deep copy
import copy

a = [[1, 2], [3, 4]]

b = a  # shallow copy
c = copy.deepcopy(a)  # deep copy

a[0][0] = 99

print("Original:", a)
print("Shallow copy:", b)
print("Deep copy:", c)