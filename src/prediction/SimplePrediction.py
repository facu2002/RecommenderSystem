
from prediction.Prediction import Prediction

from Recommender import Recommender

class SimplePrediction(Prediction):
  @staticmethod
  def predict():
    numerator = 0
    denominator = 0
    for similarity_key, similarity_value in Recommender.neighbors.items():
      numerator += similarity_value * Recommender.matrix[similarity_key[1]][Recommender.coordinate_prediction[1]]
      denominator += abs(similarity_value) 
    result = numerator / denominator
    ################## Todo
    # if result < Recommender.lower:
    #   return Recommender.lower
    
    return result
