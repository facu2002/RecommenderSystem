from metric.Metric import Metric
from math import sqrt
from Recommender import Recommender


class PearsonCorrelation(Metric):

  @staticmethod
  def similarity(recommender):
    """
    Function that calculates the similarity between two users thanks to the Pearson correlation.
    Args:
        recommender: Instance of the Recommender class where the attributes necessary for the calculation of the similarity are found.
    Returns:
    Result of similarity.
    """
    result = dict()
    for v in range(len(recommender.matrix)):
      if v == recommender.coordinate_prediction[0]:
        continue
      else:
        intersection = recommender.intersection_qualified_items(recommender.coordinate_prediction[0], v)
        mean_u = recommender.mean_rows(recommender.matrix, recommender.coordinate_prediction[0], intersection)
        mean_v = recommender.mean_rows(recommender.matrix, v, intersection)
        numerator = 0
        denominator1 = 0
        denominator2 = 0
        for i in intersection:
          numerator += ((recommender.matrix[recommender.coordinate_prediction[0]][i] - mean_u) * (recommender.matrix[v][i] - mean_v))
          denominator1 += (recommender.matrix[recommender.coordinate_prediction[0]][i] - mean_u)**2
          denominator2 += (recommender.matrix[v][i] - mean_v)**2
        if numerator == 0 and (denominator1 == 0 or denominator2 == 0):
          result[(recommender.coordinate_prediction[0],v)]  = 0
        else:
          result[(recommender.coordinate_prediction[0],v)] = numerator / (sqrt(denominator1) * sqrt(denominator2))
    return result