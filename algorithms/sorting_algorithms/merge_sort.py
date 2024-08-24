def merge_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left < right:
        middle = (left + right) // 2
        yield from merge_sort(arr, left, middle)
        yield from merge_sort(arr, middle + 1, right)
        yield from merge(arr, left, middle, right)
        yield arr

def merge(arr, left, middle, right):
    left_copy = arr[left:middle + 1]
    right_copy = arr[middle + 1:right + 1]

    left_copy_idx = 0
    right_copy_idx = 0
    sorted_idx = left

    while left_copy_idx < len(left_copy) and right_copy_idx < len(right_copy):
        if left_copy[left_copy_idx] <= right_copy[right_copy_idx]:
            arr[sorted_idx] = left_copy[left_copy_idx]
            left_copy_idx += 1
        else:
            arr[sorted_idx] = right_copy[right_copy_idx]
            right_copy_idx += 1
        sorted_idx += 1
        yield arr

    while left_copy_idx < len(left_copy):
        arr[sorted_idx] = left_copy[left_copy_idx]
        left_copy_idx += 1
        sorted_idx += 1
        yield arr

    while right_copy_idx < len(right_copy):
        arr[sorted_idx] = right_copy[right_copy_idx]
        right_copy_idx += 1
        sorted_idx += 1
        yield arr
