def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr = [5, 3, 8, 4, 2]
x = 2
result = linear_search(arr, x)

if result == -1:
    print("Element not found in array")
else:
    print("Element found at index", result)