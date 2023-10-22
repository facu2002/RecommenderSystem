from math import sqrt
from Recommender import Recommender
from metric.Metric import Metric


class EuclideanDistance(Metric):
  @staticmethod
  def similarity(recommender):
    """
    Function that calculates the similarity between two users thanks to the Euclidean distance.
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
        accumulate = 0
        for i in intersection:
          accumulate += (recommender.matrix[recommender.coordinate_prediction[0]][i]  - recommender.matrix[v][i])**2
        result[(recommender.coordinate_prediction[0], v)] = sqrt(accumulate)
    return result
