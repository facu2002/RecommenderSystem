from metric.Metric import Metric
from math import sqrt
from utils import intersection_qualified_items


class PearsonCorrelation(Metric):

  
  @staticmethod
  def similarity():
    result = dict()
    for v in range(len(Metric.matrix)):
      if v == Metric.u:
        continue
      else:
        intersection = intersection_qualified_items(Metric.matrix, Metric.u, v)
        mean_u = Metric.mean_rows(Metric.matrix, Metric.u, intersection)
        mean_v = Metric.mean_rows(Metric.matrix, v, intersection)
        numerator = 0
        denominator1 = 0
        denominator2 = 0 
        for i in intersection:
          numerator += ((Metric.matrix[Metric.u][i] - mean_u) * (Metric.matrix[v][i] - mean_v))
          denominator1 += (Metric.matrix[Metric.u][i] - mean_u)**2
          denominator2 += (Metric.matrix[v][i] - mean_v)**2
        result[(Metric.u,v)] = numerator / (sqrt(denominator1) * sqrt(denominator2))
    return result