from math import sqrt
from utils import intersection_qualified_items



def cosine_distance_coefficient(matrix, u):
  resultados = dict()
  for v in range(matrix[0][0]):
    if v == u:
      continue
    else:
      intersection = intersection_qualified_items(matrix, u, v)
      print(intersection)
      numerator = 0
      denominator1 = 0
      denominator2 = 0 
      for i in intersection:
        numerator += (matrix[1][(u,i)] * matrix[1][(v,i)] )
        denominator1 += matrix[1][(u,i)]**2
        denominator2 += matrix[1][(v,i)]**2
      resultados[f"Sim({u}, {v})"] = numerator / (sqrt(denominator1) * sqrt(denominator2))  
  return resultados
