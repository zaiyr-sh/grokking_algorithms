# Время выполнения: O(n * logn) - в среднем случае и O(n^2) - в худшем случае

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 11, 2, 14, 3]))