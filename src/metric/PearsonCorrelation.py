from metric.Metric import Metric
from math import sqrt
from Recommender import Recommender


class PearsonCorrelation(Metric):

  
  @staticmethod
  def similarity():
    result = dict()
    for v in range(len(Recommender.matrix)):
      if v == Recommender.coordinate_prediction[0]:
        continue
      else:
        intersection = Recommender.intersection_qualified_items(Recommender.coordinate_prediction[0], v)
        mean_u = Recommender.mean_rows(Recommender.matrix, Recommender.coordinate_prediction[0], intersection)
        mean_v = Recommender.mean_rows(Recommender.matrix, v, intersection)
        numerator = 0
        denominator1 = 0
        denominator2 = 0
        for i in intersection:
          numerator += ((Recommender.matrix[Recommender.coordinate_prediction[0]][i] - mean_u) * (Recommender.matrix[v][i] - mean_v))
          denominator1 += (Recommender.matrix[Recommender.coordinate_prediction[0]][i] - mean_u)**2
          denominator2 += (Recommender.matrix[v][i] - mean_v)**2
        if numerator == 0 and (denominator1 == 0 or denominator2 == 0):
          result[(Recommender.coordinate_prediction[0],v)]  = 0
        else:
          result[(Recommender.coordinate_prediction[0],v)] = numerator / (sqrt(denominator1) * sqrt(denominator2))
    return result