


def print_matrix(matrix):
  if len(matrix) == 0: ################### COntrolamos errores de este tipo?
    print(f"La matriz de {len(matrix)} X {len(matrix[0])}")
    return
  print(f"La matriz de {len(matrix)} X {len(matrix[0])}")
  for row in matrix:
    for element in row:
      print(element, end=" ")
    print()



def take_line(matrix, num_line):
  return matrix[num_line]



def intersection_qualified_items(matrix, u, v):
  intersection_items = []
  row1 = matrix[u]
  row2 = matrix[v]
  print(row1, row2, sep="\n")
  # buscamos los indices de los elementos no nulos
  return [ x for x in range(len(row1)) if matrix[u][x] is not None and matrix[v][x] is not None]
