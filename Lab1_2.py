import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


random_list = [random.randint(1, 100) for _ in range(15)]

print("Original List:")
print(random_list)

bubble_sort(random_list)

print("Sorted List:")
print(random_list)
