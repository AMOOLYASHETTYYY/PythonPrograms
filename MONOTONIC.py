def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing


arr1 = [1, 2, 2, 3]
arr2 = [5, 4, 4, 2]
arr3 = [1, 3, 2]

print(f"arr1 is monotonic: {is_monotonic(arr1)}")
print(f"arr2 is monotonic: {is_monotonic(arr2)}")
print(f"arr3 is monotonic: {is_monotonic(arr3)}")