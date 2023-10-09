

def print_matrix(matrix):
  print("(filas, columnas) :", matrix[0])
  for i in range(matrix[0][0]):
    for j in range(matrix[0][1]):
      if (i,j) in matrix[1]:
        print(matrix[1][(i,j)], end=" ")
      else:
        print("-", end=" ")
    print()
