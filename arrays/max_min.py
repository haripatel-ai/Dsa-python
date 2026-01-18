# DSA Day 2: Find Maximum and Minimum in an Array

arr = [10, 25, 3, 45, 7]

# Assume first element is max and min
max_val = arr[0]
min_val = arr[0]

# Traverse array
for x in arr:
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x

print("Array:", arr)
print("Maximum element:", max_val)
print("Minimum element:", min_val)