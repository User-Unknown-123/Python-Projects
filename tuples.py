# tuple input
t = (4, 2, 8, 1, 5)

# q1 max and min
mx = t[0]
mn = t[0]

for i in t:
    if i > mx:
        mx = i
    if i < mn:
        mn = i

print("Max:", mx)
print("Min:", mn)

print()

# q2 list of tuples to dictionary
lt = [("a", 1), ("b", 2), ("c", 3)]
d = {}

for i in lt:
    d[i[0]] = i[1]

print("Dictionary:", d)

print()

# q3 count element in tuple
x = 2
count = 0

for i in t:
    if i == x:
        count += 1

print("Count of", x, ":", count)

print()

# q4 tuple with mutable element
t2 = (1, 2, [3, 4])
t2[2][0] = 99  # changing list inside tuple

print("Modified tuple:", t2)

print()

# q5 swap two tuples
a = (1, 2)
b = (3, 4)

a, b = b, a

print("a:", a)
print("b:", b)