# Importamos las dependencias del cálculo de las similitudes
from metric.PearsonCorrelation import PearsonCorrelation
from metric.CosineDistance import CosineDistance 
from metric.EuclideanDistance import EuclideanDistance


# Importamos las dependencias del cálculo de la predicción
from prediction.SimplePrediction import SimplePrediction
from prediction.DifferenceAverage import DifferenceAverage


# Importamos la clase recomendadora
from Recommender import Recommender

# Importamos 
import argparse
import sys
import time


if len(sys.argv) != 1:
  parser = argparse.ArgumentParser()
  parser.add_argument("-f", "--filename", required=True, help="entering the name of the file you want to analyze")
  parser.add_argument("-m", "--metric", required=True, help="introduction of the type of chosen metric --> [0] Pearson Correlation [1] Euclidean Distance [2] Cosine Distance")
  parser.add_argument("-p", "--prediction", required=True, help="introduction of the type of chosen prediction --> [0] Simple Prediction [1] Difference Average")
  parser.add_argument("-n", "--num_neighbors", required=True, help="introduction of the number of neighbors for the analysis of the recommendation")  
  
  args = parser.parse_args()
  metric = int(args.metric)
  prediction = int(args.prediction)
  num_neighbors = int(args.num_neighbors)
  # Leemos el fichero de entrada de datos
  file_name = f"./data/{str(args.filename)}"
  # Controlamos el caso en el que los vecinos son menores que 1
  if (num_neighbors < 1):
    print("The value of the number of neighbors must not be less than 1")
    sys.exit(1)
  # Controlamos el caso en el que se introduce incorrectamente el índice de la métrica
  if (metric < 0 or metric > 2):
    print("\nThe values of the metric must be between 0 and 2")
    print("The possible values are : \n")
    print("[0] Pearson Correlation")
    print("[1] Euclidean Distance")
    print("[2] Cosine Distance\n")  
    sys.exit(1)
  # Controlamos el caso en el que se introduce incorrectamente el índice de la predicción
  if (prediction < 0 or prediction > 1):
    print("\nThe values of the prediction must be between 0 and 1")
    print("The possible values are : \n")
    print("[0] Simple Prediction")
    print("[1] Difference Avarage")
    sys.exit(1)
else:
  metric = -1
  prediction = -1
  num_neighbors = -1  
  dimension_examples = [(10,25), (100,1000), (25,100), (5,10), (50,250)]

  for index, dimension in enumerate(dimension_examples):
      print(f"[{index}] - {dimension}")
  option_dimension_example = -1
  while not (-1 < option_dimension_example < 5):
      option_dimension_example = int(input("Enter the dimension of the matrix you want to run\n>> "))
  option_dimension_example = dimension_examples[option_dimension_example]
  number_dataset_dimension = 0
  while not (0 < number_dataset_dimension < 11):
      number_dataset_dimension = int(input("Enter the number of dataset you want to use [1-10]\n>> "))
  file_name = f"./data/utility-matrix-{option_dimension_example[0]}-{option_dimension_example[1]}-{number_dataset_dimension}.txt"
  while num_neighbors < 1:
    num_neighbors = int(input("Indicates a number of neighbors, at least one\n>> "))
  while metric < 0 or metric > 2:
    print("Indicates the metric you want to use")
    print("The possible values are : \n")
    print("[0] Pearson Correlation")
    print("[1] Euclidean Distance")
    print("[2] Cosine Distance")
    metric = int(input(">> ")) 
  while prediction < 0 or prediction > 1:
    print("Indicates the type of prediction you want to use")
    print("The possible values are : \n")
    print("[0] Simple Prediction")
    print("[1] Difference Avarage")
    prediction = int(input(">> "))
  

  
# Elección de la métrica
if metric == 0:
  metric_function = PearsonCorrelation.similarity
elif metric == 1:
  metric_function = EuclideanDistance.similarity
elif metric == 2:
  metric_function = CosineDistance.similarity



# Elección de la predicción
if prediction == 0:
  prediction_function = SimplePrediction.predict
elif prediction == 1:
  prediction_function = DifferenceAverage.predict


# Guardamos el tiempo de inicio de ejecución
start_time = time.time()

recommender = Recommender(file_name, num_neighbors, metric_function)
result = recommender.run(prediction_function)


print("\n\nMatrices resultantes  #########################################################\n")
recommender.print_matrix(recommender.matrix)
recommender.print_matrix(recommender.unnormalized_matrix)
print()

# guardamos el tiempo de finalización de nuestra ejecución
end_time = time.time()
print(f"EL TIEMPO DE CALCULO TOTAL HA SIDO\nEN SEGUNDOS --> {end_time - start_time}\nEN MINUTOS --> {(end_time - start_time) / 60}")


