def range_bitwise_and(m, n):
    shift = 0
    # Find the common left header of m and n
    while m < n:
        m >>= 1
        n >>= 1
        shift += 1
    return m << shift
