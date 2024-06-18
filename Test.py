def get_matrix(n, m, value, k):
    matrix = []
    for i in range(n):
        matrix1 = []
        matrix.append(matrix1)
        for j in range(m):
           matrix1.append(value)
        for h in range(k):
            matrix.append(matrix)
            for j in range(m):
                matrix1.append(value)

    return matrix

result1 = get_matrix(2, 2, 10, 2)
result2 = get_matrix(3, 5, 42, 3)
result3 = get_matrix(4, 2, 13, 1)
print(result1)
print(result2)
print(result3)
