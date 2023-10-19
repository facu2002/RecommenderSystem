
def load_data(file_name):
  utility_matrix = []
  with open(file_name, "r") as file_system:
    # Rellenamos la matriz
    lines = file_system.readlines()
    lower_limit = float(lines[0])
    upper_limit = float(lines[1])
    for line in lines[2:]:
      aux_row = []
      for element in line.split():
        if '-' != element:
          aux_row.append(float(element))
        else:
          aux_row.append(None)
      utility_matrix.append(aux_row)
  return (lower_limit, upper_limit, utility_matrix)