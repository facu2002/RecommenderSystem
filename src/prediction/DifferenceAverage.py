from prediction.Prediction import Prediction

from Recommender import Recommender


class DifferenceAverage(Prediction):

  @staticmethod
  def predict():
    aux_mean_u = list(filter(lambda x: x != None, Recommender.matrix[Recommender.coordinate_prediction[0]]))
    mean_u = sum(aux_mean_u) / len(aux_mean_u)
    numerator = 0
    denominator = 0
    for similarity_key, similarity_value in Recommender.neighbors.items():
      aux_mean_v = list(filter(lambda x: x != None, Recommender.matrix[similarity_key[1]]))
      mean_v = sum(aux_mean_v) / len(aux_mean_v)
      numerator += similarity_value * (Recommender.matrix[similarity_key[1]][Recommender.coordinate_prediction[1]] - mean_v)
      denominator += abs(similarity_value)
    return mean_u + (numerator / denominator)
