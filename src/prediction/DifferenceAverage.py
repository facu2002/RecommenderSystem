from prediction.Prediction import Prediction

from Recommender import Recommender


class DifferenceAverage(Prediction):

  @staticmethod
  def predict(recommender):
    """
    Function that calculates the prediction of the value that a user provides to an item, trough the use of Difference Average.
    Args:
        recommender: Instance of the Recommender class where the attributes necessary for the calculation of the prediction are found.
    Returns:
    Result of prediction.
    """
    aux_mean_u = list(filter(lambda x: x != None, recommender.matrix[recommender.coordinate_prediction[0]]))
    mean_u = sum(aux_mean_u) / len(aux_mean_u)
    numerator = 0
    denominator = 0
    for similarity_key, similarity_value in recommender.neighbors.items():
      aux_mean_v = list(filter(lambda x: x != None, recommender.matrix[similarity_key[1]]))
      mean_v = sum(aux_mean_v) / len(aux_mean_v)
      numerator += similarity_value * (recommender.matrix[similarity_key[1]][recommender.coordinate_prediction[1]] - mean_v)
      denominator += abs(similarity_value)
    if denominator == 0:
      return 0
    result = mean_u + (numerator / denominator)
    # Aquí lo que hacemos es normalizar el limite inferior, pero como es el menor de los valores, debemos poner 0
    # ocurre lo mismo con el limite superior, que daría siempre 1, ya que al normalizarlo, los valores están entre 0 y 1
    lower_normalized = 0
    if result < lower_normalized:
      return 0
    return result
