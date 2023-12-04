def max_product(nums):
    if not nums:
        return 0

    max_prod = min_prod = result = nums[0]
    for n in nums[1:]:
        temp = max_prod
        max_prod = max(n, max_prod * n, min_prod * n)
        min_prod = min(n, temp * n, min_prod * n)
        result = max(result, max_prod)
    return result
