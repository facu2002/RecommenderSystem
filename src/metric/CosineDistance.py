from math import sqrt
from utils import intersection_qualified_items
from metric.Metric import Metric

class CosineDistance(Metric):

  @staticmethod
  def similarity():
    result = dict()
    for v in range(len(Metric.matrix)):
      if v == Metric.u:
        continue
      else:
        intersection = intersection_qualified_items(Metric.matrix, Metric.u, v)
        numerator = 0
        denominator1 = 0
        denominator2 = 0 
        for i in intersection:
          numerator += (Metric.matrix[Metric.u][i]  * Metric.matrix[v][i] )
          denominator1 += Metric.matrix[Metric.u][i]**2
          denominator2 += Metric.matrix[v][i]**2
        result[f"Sim({Metric.u}, {v})"] = numerator / (sqrt(denominator1) * sqrt(denominator2))
    return result
