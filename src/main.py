# Importamos las dependencias del cálculo de las similitudes
from metric.PearsonCorrelation import PearsonCorrelation
from metric.CosineDistance import CosineDistance 
from metric.EuclideanDistance import EuclideanDistance


# Importamos las dependencias del cálculo de la predicción
from prediction.SimplePrediction import SimplePrediction
from prediction.DifferenceAverage import DifferenceAverage


# Importamos la clase recomendadora
from Recommender import Recommender


# Leemos el fichero de entrada de datos
num_dataset = int(input("\nIndica el número de dataset a utilizar\n>> "))
file_name = f"./data/data{num_dataset}.txt"


# Leemos el número de vecinos
# num_neighbor = 0
# while num_neighbor > len(Recommender.matrix) or num_neighbor < 1:
num_neighbor = int(input("\nIndica el número de vecinos\n>> "))
  
  
# Elección de la métrica
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


# Elección de la predicción
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


print("\n\nMatrices resultantes  #####################################################\n")

recommender.print_matrix(recommender.matrix)
recommender.print_matrix(recommender.unnormalized_matrix)