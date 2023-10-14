from math import sqrt
from utils import intersection_qualified_items
from metric.Metric import Metric


class EuclideanDistance(Metric):
  @staticmethod
  def similutues(matrix, u):
    resultados = dict()
    for v in range(len(matrix)):
      if v == u:
        continue
      else:
        intersection = intersection_qualified_items(matrix, u, v)
        result = 0
        for i in intersection:
          result += (matrix[u][i]  - matrix[v][i])**2
        resultados[f"Sim({u}, {v})"] = sqrt(result)
    return resultados
