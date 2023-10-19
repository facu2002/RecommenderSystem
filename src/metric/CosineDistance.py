from math import sqrt
from Recommender import Recommender
from metric.Metric import Metric

class CosineDistance(Metric):

  @staticmethod
  def similarity(recommender):
    result = dict()
    for v in range(len(recommender.matrix)):
      if v == recommender.coordinate_prediction[0]:
        continue
      else:
        intersection = recommender.intersection_qualified_items(recommender.coordinate_prediction[0], v)
        numerator = 0
        denominator1 = 0
        denominator2 = 0 
        for i in intersection:
          numerator += (recommender.matrix[recommender.coordinate_prediction[0]][i]  * recommender.matrix[v][i] )
          denominator1 += recommender.matrix[recommender.coordinate_prediction[0]][i]**2
          denominator2 += recommender.matrix[v][i]**2
        result[(0, v)] = numerator / (sqrt(denominator1) * sqrt(denominator2))
    return result
