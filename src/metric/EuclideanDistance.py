from math import sqrt
from utils import intersection_qualified_items
from metric.Metric import Metric


class EuclideanDistance(Metric):
  @staticmethod
  def similarity():
    result = dict()
    for v in range(len(Metric.matrix)):
      if v == Metric.u:
        continue
      else:
        intersection = intersection_qualified_items(Metric.matrix, Metric.u, v)
        result = 0
        for i in intersection:
          result += (Metric.matrix[Metric.u][i]  - Metric.matrix[v][i])**2
        result[f"Sim({Metric.u}, {v})"] = sqrt(result)
    return result
