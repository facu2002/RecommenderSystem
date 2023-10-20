
from prediction.Prediction import Prediction

from Recommender import Recommender

class SimplePrediction(Prediction):
  @staticmethod
  def predict(recommender):
    numerator = 0
    denominator = 0
    print("EL neigbors tiene ", recommender.neighbors, "Ademas vemos que estamos prediciendo", recommender.coordinate_prediction)
    for similarity_key, similarity_value in recommender.neighbors.items():
      numerator += similarity_value * recommender.matrix[similarity_key[1]][recommender.coordinate_prediction[1]]
      denominator += abs(similarity_value)
    if denominator == 0:
      return 0 
    result = numerator / denominator

    # Aquí lo que hacemos es normalizar el limite inferior, pero como es el menor de los valores, debemos poner 0
    # ocurre lo mismo con el limite superior, que daría siempre 1, ya que al normalizarlo, los valores están entre 0 y 1
    lower_normalized = 0
    if result < lower_normalized:
      return 0
    
    return result
