class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_representation = '\n'
        for row in self.matrix:
            for el in row:
                matrix_representation += f"{el:>10}"
            matrix_representation += "\n"
        return matrix_representation

    def __add__(self, other):
        result = []
        if len(self.matrix) != len(other.matrix):
            print("Невозможно произвести суммирование (не одинаковое количество строк)")
            return
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                print("Невозможно произвести суммирование (не одинаковое количество столбцов)")
                return
            row = []
            for j in range(len(self.matrix[i])):
                new_list = self.matrix[i],[j] + other.matrix[i],[j]
                row.append(new_list)
            result.append(row)

        return Matrix(result)

matr1 = Matrix([[1,2,3],[1,2,3]])
print(f"matr1 = {matr1}")
matr2 = Matrix([[1, 5, 3], [1, 6, 8]])
print(f"matr2 = {matr2}")
print(f"matr3 = {matr1 + matr2}")

