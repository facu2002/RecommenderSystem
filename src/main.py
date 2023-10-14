from file_system import load_data
from utils import intersection_qualified_items, print_matrix
from metric.pearson_correlation import pearson_correlation_coefficient
from metric.cosine_distance import cosine_distance_coefficient
from metric.euclidean_distance import euclidean_distance
from prediction.simple_prediction import simple_prediction


from metric.Metric import Metric



num_dataset = int(input("Indica el número de dataset a utilizar\n>> "))
# Leemos el fichero
file_name = f"./data/data{num_dataset}.txt"

# (tuple, dict)  -> ((numero_filas, numero_columnas), {valores_matriz}
utility_matrix = load_data(file_name)

print_matrix(utility_matrix)


# PRUEBAS DE CLASES

print(Metric.pearson_correlation_coefficient(utility_matrix, 0))
print(Metric.pearson_correlation_coefficient(utility_matrix, 0))
print(Metric.pearson_correlation_coefficient(utility_matrix, 0))







# option = int(input("¿Qué Métrica desea? Los posibles valores son:\n[1] Correlación de Pearson.\n[2] Distancia coseno.\n[3] Distancia Euclídea.\n>> "))

# if option == 1:
#   print(pearson_correlation_coefficient(utility_matrix, 0))
# elif option == 2:
#   print(cosine_distance_coefficient(utility_matrix, 0))
# else:
#   print(euclidean_distance(utility_matrix, 0))

# # num_neighbors = int(input("Indica el número de vecinos a considerar\n>> "))

# print(simple_prediction(utility_matrix, 0, pearson_correlation_coefficient(utility_matrix, 0)))