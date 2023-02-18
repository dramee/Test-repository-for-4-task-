array1 = [12, 32, 35, 41, 52, 67, 90, 112, 131, 315, 123, 31231, 3123151, 3131]


def search(nums, target):
    left = 0
    right = len(nums)

    while left <= right:
        curr_ind = (left + right) // 2
        if nums[curr_ind] == target:
            return curr_ind
        elif nums[curr_ind] < target:
            left = curr_ind + 1
        else:
            right = curr_ind - 1
    return -1


print(search(array, 41))
print(search(array, 31) == -1)
print(search(array, 3123))
