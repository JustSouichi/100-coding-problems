def max_subarray_sum(arr):
    if not arr:
        return 0

    max_so_far = arr[0]
    curr_max = arr[0]

    for num in arr[1:]:
        curr_max = max(num, curr_max + num)
        max_so_far = max(max_so_far, curr_max)

    return max_so_far
