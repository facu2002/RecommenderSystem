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




recommender = Recommender(file_name, num_neighbors, metric_function)
result = recommender.run(prediction_function)



print("\n\nMatrices resultantes  #########################################################\n")
recommender.print_matrix(recommender.matrix)
recommender.print_matrix(recommender.unnormalized_matrix)
print()