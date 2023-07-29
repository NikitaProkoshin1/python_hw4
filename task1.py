#Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]
matrix = [[1, 2, 3],
          [4, 5, 6]]

print("исходная матрица:\n", matrix)

def matrix_transposition(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    print(trans_matrix)
print("транспонированная матрица:")
matrix_transposition(matrix)
