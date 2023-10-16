from file_system import load_data


class Recommender: 
  matrix = []
  neighbors = []
  coordinate_prediction = (None, None)
  def __init__(self, file_name, num_neighbors, similarity_function):
    Recommender.coordinate_prediction = (0, 4)
    Recommender.matrix = load_data(file_name)
    Recommender.neighbors = Recommender.get_neighbors(num_neighbors, similarity_function())
    
  def run(self, prediction_function):
    return prediction_function()
    
    
  def print_matrix(matrix):
    if len(matrix) == 0:
      print(f"La matriz de {len(matrix)} X {len(matrix[0])}")
      return
    print(f"La matriz de {len(matrix)} X {len(matrix[0])}")
    for row in matrix:
      for element in row:
        print(element, end=" ")
      print()


  def mean_rows(matrix, user, intersecting_columns):
    if len(intersecting_columns) != 0:
      sum = 0
      for i in range(len(matrix[0])):
        if i in intersecting_columns:
          sum += matrix[user][i]
      return sum / len(intersecting_columns)
    return 0


  def intersection_qualified_items(u, v):
    intersection_items = []
    row1 = Recommender.matrix[u]
    row2 = Recommender.matrix[v]
    # buscamos los indices de los elementos no nulos
    return [ x for x in range(len(row1)) if Recommender.matrix[u][x] is not None and Recommender.matrix[v][x] is not None]


  @staticmethod
  def get_neighbors(num_neighbor, similarity):
    # Ordena el diccionario por los valores de forma descendente
    ordered_similarity = sorted(similarity, key=lambda x: similarity[x], reverse=True)
    neighbors = {x: (similarity[x]) for x in ordered_similarity[:num_neighbor]}
    # Devuelve las primeras n claves
    return neighbors
