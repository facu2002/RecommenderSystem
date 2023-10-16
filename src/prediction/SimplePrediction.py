
from utils import intersection_qualified_items
from prediction.Prediction import Prediction

class SimplePrediction(Prediction):
  
  @staticmethod
  def predict():
    numerador = 0
    aux = [abs(Prediction.neighbors[(Prediction.u,v)]) for v in range(len(Prediction.neighbors) + 1) if v != Prediction.u]
    print("El aux es ", aux)
    denominador = sum(aux)
    print("La suma de las similitudes es -> ", denominador)
    for v in range(len(Prediction.neighbors)):
      if v == Prediction.u:
        continue
      else:
        intersection = intersection_qualified_items(Prediction.matrix, Prediction.u, v)
        for i in intersection:
          numerador += Prediction.neighbors[(Prediction.u,v)] * Prediction.matrix[v][i]
          
    print("HOLA EZ%R ES ", numerador / denominador)