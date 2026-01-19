# DSA Day 3: Count Even and Odd Numbers

arr = [10, 21, 32, 43, 54]

even_count = 0
odd_count = 0

for x in arr:
    if x % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Array:", arr)
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)