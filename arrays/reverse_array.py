# DSA Day 3: Reverse an Array

arr = [1, 2, 3, 4, 5]

print("Original array:", arr)

n = len(arr)
for i in range(n // 2):
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

print("Reversed array:", arr)