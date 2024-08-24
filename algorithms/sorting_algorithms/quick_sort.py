def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Correctly partition the array and get the partition index
        pi = partition(arr, low, high)
        yield from quick_sort(arr, low, pi - 1)
        yield from quick_sort(arr, pi + 1, high)
        yield arr

def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            yield arr  # Yield the array state after each swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr  # Yield the array state after the final swap
    return i + 1  # Return the partition index as an integer
