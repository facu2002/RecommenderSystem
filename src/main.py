from file_system import load_data
from utils import intersection_qualified_items, print_matrix, get_neighbor


from metric.Metric import Metric
from metric.PearsonCorrelation import PearsonCorrelation
from metric.CosineDistance import CosineDistance

from prediction.Prediction import Prediction
from prediction.SimplePrediction import SimplePrediction
from prediction.DifferenceAverage import DifferenceAverage


num_dataset = int(input("Indica el número de dataset a utilizar\n>> "))
# Leemos el fichero
file_name = f"./data/data{num_dataset}.txt"

# (tuple, dict)  -> ((numero_filas, numero_columnas), {valores_matriz}
utility_matrix = load_data(file_name)

print_matrix(utility_matrix)


# PRUEBAS DE CLASES

Metric.matrix = utility_matrix
Metric.u = 0


print(PearsonCorrelation.similarity())

num_neighbor = int(input("Indica el número de vecinos\n>> "))

neighbors = get_neighbor(num_neighbor, PearsonCorrelation.similarity())

print(neighbors)

Prediction.matrix = utility_matrix
Prediction.neighbors = neighbors
Prediction.u = 0

print(SimplePrediction.predict())

