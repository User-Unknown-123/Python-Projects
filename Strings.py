s = input("Enter a string: ")

# q1 count things
v = 0
c = 0
d = 0
sp = 0

for i in s:
    if i.lower() in "aeiou":
        v += 1
    elif i.isalpha():
        c += 1
    elif i.isdigit():
        d += 1
    else:
        sp += 1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Special:", sp)

print()

# q2 reverse each word
words = s.split()
new = []

for w in words:
    new.append(w[::-1])

print("Reversed words:", " ".join(new))

print()

# q3 palindrome check
st = s.replace(" ", "").lower()

if st == st[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

print()

# q4 character frequency
f = {}

for ch in s:
    if ch in f:
        f[ch] += 1
    else:
        f[ch] = 1

print("Frequency:")
for k in f:
    print(k, f[k])

print()

# q5 string immutability
try:
    s[0] = 'a'
except TypeError:
    print("String cannot be changed")
