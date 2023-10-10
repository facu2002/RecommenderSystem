from math import sqrt
from utils import intersection_qualified_items


def euclidean_distance(matrix, u):
  resultados = dict()
  for v in range(matrix[0][0]):
    if v == u:
      continue
    else:
      intersection = intersection_qualified_items(matrix, u, v)
      print(intersection)
      result = 0
      for i in intersection:
        result += (matrix[1][(u,i)] - matrix[1][(v,i)])**2
      resultados[f"Sim({u}, {v})"] = sqrt(result)
  return resultados
