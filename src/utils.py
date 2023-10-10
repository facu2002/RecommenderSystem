

def print_matrix(matrix):
  print("(filas, columnas) :", matrix[0])
  for i in range(matrix[0][0]):
    for j in range(matrix[0][1]):
      if (i,j) in matrix[1]:
        print(matrix[1][(i,j)], end=" ")
      else:
        print("-", end=" ")
    print()


def take_line(matrix, num_line):
  line = dict()
  for i in range(matrix[0][1]):
    if (num_line, i) in matrix[1]:
      line[(num_line, i)] = (matrix[1][(num_line, i)])
  return line



# u y v conceptualmente representan los usuarios, en nuestro programa, representan las filas de las valoraciones de los usuarios
def intersection_qualified_items(matrix, u, v):
  intersection_items = []
  # pedir la fila 1
  row1 = take_line(matrix, u)

  # pedir la fila 2
  row2 = take_line(matrix, v)

  # recorremos el for en base al numero de columnas
  for i in range(matrix[0][1]):
    if (u, i) in row1 and (v, i) in row2:
      intersection_items.append(i)
  
  return intersection_items
