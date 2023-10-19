from prediction.Prediction import Prediction

from Recommender import Recommender


class DifferenceAverage(Prediction):

  @staticmethod
  def predict(recommender):
    aux_mean_u = list(filter(lambda x: x != None, recommender.matrix[recommender.coordinate_prediction[0]]))
    mean_u = sum(aux_mean_u) / len(aux_mean_u)
    numerator = 0
    denominator = 0
    for similarity_key, similarity_value in recommender.neighbors.items():
      aux_mean_v = list(filter(lambda x: x != None, recommender.matrix[similarity_key[1]]))
      mean_v = sum(aux_mean_v) / len(aux_mean_v)
      numerator += similarity_value * (recommender.matrix[similarity_key[1]][recommender.coordinate_prediction[1]] - mean_v)
      denominator += abs(similarity_value)
    return mean_u + (numerator / denominator)
