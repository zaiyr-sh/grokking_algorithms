def binary_search(nums, item):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


nums = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(nums, 6))