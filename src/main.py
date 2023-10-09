from file_system import load_data
from utils import print_matrix
from math import sqrt

# Leemos el fichero
file_name = "./data/data2.txt"

# (tuple, dict)  -> ((numero_filas, numero_columnas), {valores_matriz}
utility_matrix = load_data(file_name)

# print_matrix(utility_matrix)

def mean_columns(matrix, u, columns):
  sum = 0
  for i in range(matrix[0][1]):
    if i in columns:
      sum += matrix[1][(u,i)]
  return sum / len(columns)


def take_line(matrix, num_line):
  line = dict()
  for i in range(matrix[0][1]):
    if (num_line, i) in matrix[1]:
      line[(num_line, i)] = (matrix[1][(num_line, i)])
  return line
      


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


def pearson_correlation_coefficient(matrix, u):
  resultados = dict()
  for v in range(matrix[0][1]):
    if v == u:
      continue
    else:
      intersection = intersection_qualified_items(matrix, u, v)
      print(intersection)
      mean_u = mean_columns(matrix, u, intersection)
      mean_v = mean_columns(matrix, v, intersection)
      numerator = 0
      denominator1 = 0 
      denominator2 = 0 
      for i in intersection:
        numerator += ((matrix[1][(u,i)] - mean_u) * (matrix[1][(v,i)] - mean_v))
        denominator1 += (matrix[1][(u,i)] - mean_u)**2
        denominator2 += (matrix[1][(v,i)] - mean_v)**2
      resultados[f"Sim({u}, {v})"] = numerator / (sqrt(denominator1) * sqrt(denominator2))  
  return resultados



print(pearson_correlation_coefficient(utility_matrix, 0))



# print(take_line(utility_matrix, 0))
# print(intersection_qualified_items(utility_matrix, 0,1))
# print(mean_columns(utility_matrix, 0, intersection_qualified_items(utility_matrix, 0,1)))
# print(mean_columns(utility_matrix, 1, intersection_qualified_items(utility_matrix, 0,1)))