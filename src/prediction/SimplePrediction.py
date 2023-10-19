
from prediction.Prediction import Prediction

from Recommender import Recommender

class SimplePrediction(Prediction):
  @staticmethod
  def predict(recommender):
    numerator = 0
    denominator = 0
    for similarity_key, similarity_value in recommender.neighbors.items():
      numerator += similarity_value * recommender.matrix[similarity_key[1]][recommender.coordinate_prediction[1]]
      denominator += abs(similarity_value) 
    result = numerator / denominator
    ################## Todo
    # if result < Recommender.lower:
    #   return Recommender.lower
    
    return result
