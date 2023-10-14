from metric.Metric import Metric
from math import sqrt
from utils import intersection_qualified_items


class PearsonCorrelation(Metric):
  @staticmethod
  def mean_rows(matrix, u, intersecting_columns):
    if len(intersecting_columns) != 0:
      sum = 0
      for i in range(len(matrix[0])):
        if i in intersecting_columns:
          sum += matrix[u][i]
      return sum / len(intersecting_columns)
    return 0
  
  
  @staticmethod
  def similutues(matrix, u):
    result = dict()
    for v in range(len(matrix)):
      if v == u:
        continue
      else:
        intersection = intersection_qualified_items(matrix, u, v)
        mean_u = Metric.mean_rows(matrix, u, intersection)
        mean_v = Metric.mean_rows(matrix, v, intersection)
        numerator = 0
        denominator1 = 0
        denominator2 = 0 
        for i in intersection:
          numerator += ((matrix[u][i] - mean_u) * (matrix[v][i] - mean_v))
          denominator1 += (matrix[u][i] - mean_u)**2
          denominator2 += (matrix[v][i] - mean_v)**2
        result[(u,v)] = numerator / (sqrt(denominator1) * sqrt(denominator2))
    return result