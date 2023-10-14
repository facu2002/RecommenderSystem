from math import sqrt
from utils import intersection_qualified_items
from metric.Metric import Metric

class CosineDistance(Metric):

  @staticmethod
  def similutues(matrix, u):
    resultados = dict()
    for v in range(len(matrix)):
      if v == u:
        continue
      else:
        intersection = intersection_qualified_items(matrix, u, v)
        numerator = 0
        denominator1 = 0
        denominator2 = 0 
        for i in intersection:
          numerator += (matrix[u][i]  * matrix[v][i] )
          denominator1 += matrix[u][i]**2
          denominator2 += matrix[v][i]**2
        resultados[f"Sim({u}, {v})"] = numerator / (sqrt(denominator1) * sqrt(denominator2))
    return resultados
