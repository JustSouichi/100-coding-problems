def generate_pascals_triangle(num_rows):
    triangle = []
    for row_num in range(num_rows):
        row = [1] * (row_num + 1)
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)
    return triangle