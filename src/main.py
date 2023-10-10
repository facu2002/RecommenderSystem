from file_system import load_data
from utils import print_matrix
from metric.pearson_correlation import pearson_correlation_coefficient

# Leemos el fichero
file_name = "./data/data3.txt"

# (tuple, dict)  -> ((numero_filas, numero_columnas), {valores_matriz}
utility_matrix = load_data(file_name)


print(pearson_correlation_coefficient(utility_matrix, 2))

# print_matrix(utility_matrix)
# print(intersection_qualified_items(utility_matrix, 2, 3))

# print(take_line(utility_matrix, 0))
# print(intersection_qualified_items(utility_matrix, 0, 1))
# print(mean_rows(utility_matrix, 0, intersection_qualified_items(utility_matrix, 0,1)))
# print(mean_rows(utility_matrix, 1, intersection_qualified_items(utility_matrix, 0,1)))