
def load_data(file_name):
  utility_matrix = []
  with open(file_name, "r") as file_system:
    # Rellenamos la matriz
    lines = file_system.readlines()
    for line in lines[2:]:
      aux_row = []
      for element in line.split():
        if '-' != element:
          aux_row.append(float(element))
        else:
          aux_row.append(None)
      utility_matrix.append(aux_row)
  return utility_matrix

  
