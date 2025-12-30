text = "Python"
print(text[0])  # Output: P
print(text[1])  # Output: y
print(text[-1]) # Output: n (last character)
print(text[-2]) # Output: o

print("\nSlicing allows you to extract a portion of a string using the syntax string[start:stop:step]\n")
text = "Hello, Python!"
print(text[0:5])   # Output: Hello
print(text[:5])    # Output: Hello (same as text[0:5])
print(text[7:])    # Output: Python! (from index 7 to end)
print(text[::2])   # Output: Hlo Pto!
print(text[-6:-1]) # Output: ython (negative indexing)
print(text[0:6])
print(text[0:12])
print(text[0:14])
print(text[0:14:2])# it will skip 1 like n-1
print(text[0:14:3])
print(text[-14:-1])

print("\nThe step parameter defines the interval of slicing.\n")

text = "Python Programming"
print(text[::2])   # Output: Pto rgamn
print(text[::-1])  # Output: gnimmargorP nohtyP (reverses string)
print(text[0:14:2])# it will skip 1 like n-1
print(text[0:14:3])
