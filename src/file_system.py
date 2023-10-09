

def load_data(file_name):
  utility_matrix = ()
  with open(file_name, "r") as file_system:
    matrix = dict()
    # Obtenemos el rango inferior
    lower_rank = float(file_system.readline())
    # Obtenemos el rango superior
    top_rank = float(file_system.readline())
    # Obtenemos la matriz
    i = 0
    j = 0
    lines = file_system.readlines()
    size = (len(lines), len(lines[0].split()))
    for i, line in enumerate(lines):
      for j, element in enumerate(line.split()):
        if '-' != element:
          matrix[(i, j)] = float(element)  
    utility_matrix = (size,  matrix)
  return utility_matrix
