def second_largest(arr):
    arr = set(arr)  # Remove duplicates
    arr.remove(max(arr))
    return max(arr)

