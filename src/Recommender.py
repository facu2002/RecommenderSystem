import heapq
from file_system import load_data


class Recommender:
  lower = None
  upper = None
  matrix = []
  unnormalized_matrix = []
  neighbors = []
  coordinate_prediction = (None, None)
  
  
  def __init__(self, file_name, num_neighbors, similarity_function):
    # Recommender.lower, Recommender.upper, Recommender.matrix = load_data(file_name)
    Recommender.lower, Recommender.upper, Recommender.unnormalized_matrix = load_data(file_name)
    Recommender.matrix = self.normalize(Recommender.unnormalized_matrix)
    self.num_neighbors = num_neighbors
    self.similarity_function = similarity_function
    self.prediction_queue = None

  def run(self, prediction_function):
    print("\n#####################################################")
    print("\nMatriz Inicial")
    print("\n#####################################################")

    self.print_matrix()
    self.calculate_prediction_queue()
    iterator = 0
    while self.prediction_queue:
      Recommender.coordinate_prediction  = self.prediction_queue.pop(0)
      Recommender.neighbors = Recommender.get_neighbors(self.num_neighbors, self.similarity_function())
      if len(Recommender.neighbors) == 0:
        self.prediction_queue.append(Recommender.coordinate_prediction)
        continue
      print("Los vecinos son: ", Recommender.neighbors)
      result = prediction_function()
      Recommender.matrix[Recommender.coordinate_prediction[0]][Recommender.coordinate_prediction[1]] = result
      print("\n#####################################################")
      print(f"\nMatriz en la iteración {iterator}")
      print("\n#####################################################")
      self.print_matrix()
      iterator += 1
    
    Recommender.unnormalized_matrix = self.denormalize(Recommender.matrix)
    return Recommender.matrix    


  def print_matrix(self, out_file="output.txt"):
    with open(out_file, "w") as file:
      
      aux = f"\nLa matriz de {len(Recommender.matrix)} X {len(Recommender.matrix[0])}\n"
      aux += f"El rango de los valores es {Recommender.lower} - {Recommender.upper}\n"
      print(aux, file=file)
      print(aux)

      if len(Recommender.matrix) == 0:
        return
      for row in Recommender.matrix:
        for element in row:
          if element == None:
            print(f"{'-':<6}", end=" ", file=file)
            print(f"{'-':<6}", end=" ")
          else:
            print(f"{element:<6}", end=" ", file=file)
            print(f"{element:<6}", end=" ")  
        print()
        print("", file=file)

  def print_unnormalized_matrix(self, out_file="output.txt"):
    with open(out_file, "w") as file:
      
      aux = f"\nLa matriz de {len(Recommender.unnormalized_matrix)} X {len(Recommender.unnormalized_matrix[0])}\n"
      aux += f"El rango de los valores es {Recommender.lower} - {Recommender.upper}\n"
      # print(aux, file=file)
      print(aux)

      if len(Recommender.unnormalized_matrix) == 0:
        return
      for row in Recommender.unnormalized_matrix:
        for element in row:
          if element == None:
            # print(f"{'-':<6}", end=" ", file=file)
            print(f"{'-':<6}", end=" ")
          else:
            # print(f"{element:<6}", end=" ", file=file)
            print(f"{element:<6}", end=" ")  
        print()
        # print("", file=file)



  def mean_rows(matrix, user, intersecting_columns):
    if len(intersecting_columns) != 0:
      sum = 0
      for i in range(len(matrix[0])):
        if i in intersecting_columns:
          sum += matrix[user][i]
      return sum / len(intersecting_columns)
    return 0


  @staticmethod
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
    neighbors = dict()
    if num_neighbor == 0:
      return neighbors
    for x in ordered_similarity:
      if Recommender.matrix[x[1]][Recommender.coordinate_prediction[1]] != None:
        neighbors[x] = similarity[x]
        num_neighbor -= 1
      if num_neighbor <= 0:
        break
    return neighbors
  
  @staticmethod
  def calculate_priority(row):
    return sum(1 for elemento in row if elemento is None)


  # def calculate_prediction_queue(self):
  #   # Crear una lista de tuplas donde el primer elemento es la prioridad y el segundo es la fila
  #   priority_rows = [(Recommender.calculate_priority(row), index) for index, row in enumerate(Recommender.matrix)]
  #   # Convertir la lista en una cola de prioridad (heap)
  #   heapq.heapify(priority_rows)
  #   self.prediction_queue = priority_rows

  # def calculate_prediction_queue(self):
  #   # Crear una lista de tuplas donde el primer elemento es la prioridad y el segundo es la fila
  #   priority_rows = [(Recommender.calculate_priority(row), index) for index, row in enumerate(Recommender.matrix)]
  #   # Convertir la lista en una cola de prioridad (heap)
  #   self.prediction_queue = sorted(priority_rows, key=lambda x: x[0])

  def calculate_prediction_queue(self):
    # Crear una lista de tuplas donde el primer elemento es la prioridad y el segundo es la fila
    priority_rows = [(Recommender.calculate_priority(row), index) for index, row in enumerate(Recommender.matrix)]
    # Convertir la lista en una cola de prioridad (heap)
    indices_none = []
    for row in sorted(priority_rows, key=lambda x: x[0]):
      indices_none += [(row[1],indice) for indice, valor in enumerate(Recommender.matrix[row[1]]) if valor is None]
    self.prediction_queue = indices_none



  def normalize(self, matrix):
    result = []
    for row_aux in matrix:
      row = []
      for i in range(len(row_aux)):
        if row_aux[i] != None:
          row.append((row_aux[i] - Recommender.lower) / (Recommender.upper - Recommender.lower))
        else:
          row.append(None)
      result.append(row)
    return result
  
  
  def denormalize(self, matrix):
    result = []
    for row_aux in matrix:
      row = []
      for i in range(len(row_aux)):
        if row_aux[i] != None:
          row.append((row_aux[i] * (Recommender.upper - Recommender.lower)) + Recommender.lower)
        else:
          row.append(None)
      result.append(row)
    return result