from file_system import load_data
from utils import print_matrix

# Leemos el fichero
file_name = "./data/data1.txt"

# (tuple, dict)  -> ((numero_filas, numero_columnas), {valores_matriz}
utility_matrix = load_data(file_name)


print_matrix(utility_matrix)