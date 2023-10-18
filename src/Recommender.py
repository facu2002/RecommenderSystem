import heapq
from file_system import load_data


class Recommender:
  lower = None
  upper = None
  matrix = []
  neighbors = []
  coordinate_prediction = (None, None)
  
  
  def __init__(self, file_name, num_neighbors, similarity_function):
    # Recommender.coordinate_prediction = (0, 4)
    Recommender.lower, Recommender.upper, Recommender.matrix = load_data(file_name)
    self.num_neighbors = num_neighbors
    self.similarity_function = similarity_function
    # Recommender.neighbors = Recommender.get_neighbors(num_neighbors, similarity_function())
    self.prediction_queue = None



  def run(self, prediction_function):
    print("\nMatriz Inicial\n")
    self.print_matrix()
    self.calculate_prediction_queue()
    while self.prediction_queue:
      prioridad, fila = heapq.heappop(self.prediction_queue)
      print("LA COLA ES ACTUALMENTE -->", self.prediction_queue) 
      if prioridad != 0:
        Recommender.coordinate_prediction = (fila, Recommender.matrix[fila].index(None))
        Recommender.neighbors = Recommender.get_neighbors(self.num_neighbors, self.similarity_function())
        if len(Recommender.neighbors) == 0:
          print("EY AQUI HA OCURRIDO EL CASO ESPECIAL", Recommender.coordinate_prediction, "y entonces", (prioridad, fila), "Lo vuelvo a meter a la cola")
          heapq.heappush(self.prediction_queue, (prioridad, fila))
          return
          
        result = round(prediction_function(), 2)
        Recommender.matrix[Recommender.coordinate_prediction[0]][Recommender.coordinate_prediction[1]] = result
        self.calculate_prediction_queue()
        # print(f"\nMatriz Actualizada en la posición {Recommender.coordinate_prediction}\n")
        # self.print_matrix()        
    print("\nMatriz Final\n")
    self.print_matrix()
    #return prediction_function()
    
    

  def print_matrix(self):
    if len(Recommender.matrix) == 0:
      print(f"La matriz de {len(Recommender.matrix)} X {len(Recommender.matrix[0])}")
      return
    print(f"La matriz de {len(Recommender.matrix)} X {len(Recommender.matrix[0])}")
    for row in Recommender.matrix:
      for element in row:
        if element == None:
          print(f"{'-':<6}", end=" ")
        else:
          print(f"{element:<6}", end=" ")  
      print()


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
        neighbors[x] = (similarity[x])
        num_neighbor -= 1
    # neighbors = {x: (similarity[x]) for x in ordered_similarity[:num_neighbor]}
    # Devuelve las primeras n claves
    return neighbors
  
  @staticmethod
  def calculate_priority(row):
    return sum(1 for elemento in row if elemento is None)


  def calculate_prediction_queue(self):
    # Crear una lista de tuplas donde el primer elemento es la prioridad y el segundo es la fila
    priority_rows = [(Recommender.calculate_priority(row), index) for index, row in enumerate(Recommender.matrix)]
    # Convertir la lista en una cola de prioridad (heap)
    heapq.heapify(priority_rows)
    self.prediction_queue = priority_rows
  
  def nombre_facu():
    print("Esta prueba la esta realizando ", Recommender.coordinate_prediction )
    print("")
    for neighbor in Recommender.neighbors:
      print("     veamo sus vecinos nos dicen que", Recommender.matrix[neighbor[1]][Recommender.coordinate_prediction[1]])
      if Recommender.matrix[neighbor[1]][Recommender.coordinate_prediction[1]] == None:
        return True
    return False
      
