# taking input
s1 = set(map(int, input("Enter elements of set 1: ").split()))
s2 = set(map(int, input("Enter elements of set 2: ").split()))

# q1 set operations
print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference (s1 - s2):", s1 - s2)
print("Symmetric Difference:", s1 ^ s2)

print()

# q2 remove common elements
common = s1 & s2
s1 = s1 - common
s2 = s2 - common

print("Set 1 after removing common:", s1)
print("Set 2 after removing common:", s2)

print()

# q3 subset check
if s1.issubset(s2):
    print("Set 1 is subset of Set 2")
else:
    print("Set 1 is NOT subset of Set 2")

print()

# q4 print elements greater than a number
n = int(input("Enter a number: "))

print("Elements greater than", n)
for i in s2:
    if i > n:
        print(i)

print()

# q5 list to set and back to list
lst = list(map(int, input("Enter list elements: ").split()))

unique_list = list(set(lst))

print("List without duplicates:", unique_list)