def find_kth_largest(nums, k):
    import heapq
    return heapq.nlargest(k, nums)[-1]
