from math import sqrt
from Recommender import Recommender
from metric.Metric import Metric


class EuclideanDistance(Metric):
  @staticmethod
  def similarity():
    result = dict()
    for v in range(len(Recommender.matrix)):
      if v == Recommender.coordinate_prediction[0]:
        continue
      else:
        intersection = Recommender.intersection_qualified_items(Recommender.coordinate_prediction[0], v)
        accumulate = 0
        for i in intersection:
          accumulate += (Recommender.matrix[Recommender.coordinate_prediction[0]][i]  - Recommender.matrix[v][i])**2
        result[(Recommender.coordinate_prediction[0], v)] = sqrt(accumulate)
    return result
