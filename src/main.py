from file_system import load_data


from metric.Metric import Metric
from metric.PearsonCorrelation import PearsonCorrelation
from metric.CosineDistance import CosineDistance 
from metric.EuclideanDistance import EuclideanDistance


from prediction.Prediction import Prediction

from prediction.SimplePrediction import SimplePrediction
from prediction.DifferenceAverage import DifferenceAverage


from Recommender import Recommender


num_dataset = int(input("\nIndica el número de dataset a utilizar\n>> "))
# Leemos el fichero
file_name = f"./data/data{num_dataset}.txt"

num_neighbor = int(input("\nCONTROLAR QUE SEA MAYOR QUE 0 Y MENOR QUE N-1 Indica el número de vecinos\n>> "))


metric_option = -1
while metric_option < 0 or metric_option > 2:
  print("\n[0] Correlación Pearson")
  print("[1] Distancia Euclídea")
  print("[2] Distancia Coseno")
  aux = input("\nIndica el número de la métrica\n>> ")
  metric_option = int(aux) if aux.isdigit() else -1
  if metric_option == 0:
    metric_function = PearsonCorrelation.similarity
  elif metric_option == 1:
    metric_function = EuclideanDistance.similarity
  elif metric_option == 2:
    metric_function = CosineDistance.similarity
  else:
    print("\nSelección incorrecta")



prediction_option = -1
while prediction_option < 0 or prediction_option > 1:
  print("\n[0] Predicción simple")
  print("[1] Diferencia con la media")
  aux = input("\nIndica el número de la predicción\n>> ")
  prediction_option =  int(aux) if aux.isdigit() else -1
  if prediction_option == 0:
    prediction_function = SimplePrediction.predict
  elif prediction_option == 1:
    prediction_function = DifferenceAverage.predict
  else:
    print("\nSelección incorrecta")




recommender = Recommender(file_name, num_neighbor, metric_function)

result = recommender.run(prediction_function)

print(result)