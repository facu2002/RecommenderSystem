import heapq
from file_system import load_data


class Recommender:
  def __init__(self, file_name, num_neighbors, similarity_function):
    # Se inicializan los valores necesarios y se normaliza la matriz
    self.lower, self.upper, self.unnormalized_matrix = load_data(file_name)
    self.matrix = self.normalize(self.unnormalized_matrix)
    self.num_neighbors = num_neighbors
    self.similarity_function = similarity_function
    self.prediction_queue = None



  def run(self, prediction_function):
    print("\n\nMatriz inicial  ###############################################################\n")        
    self.print_matrix(self.matrix)
    self.calculate_prediction_queue()

    iterator = 0
    while self.prediction_queue:
      self.coordinate_prediction = self.prediction_queue.pop(0)
      self.neighbors = self.get_neighbors(self.num_neighbors, self.similarity_function(self))
      if len(self.neighbors) == 0:
        self.prediction_queue.append(self.coordinate_prediction)
        continue
      result = prediction_function(self)
      self.matrix[self.coordinate_prediction[0]][self.coordinate_prediction[1]] = result
      print(f"\n\nMatriz en la iteración {iterator}  #####################################################\n")    
      self.print_matrix(self.matrix)
      print("\nLa posición que se acaba de predecir es", self.coordinate_prediction, " : ", result)
      print("\nLas similitudes son ", self.similarity_function(self))
      print("\nLos vecinos seleccionados son ", self.neighbors)
      iterator += 1
    self.unnormalized_matrix = self.denormalize(self.matrix)
    return self.matrix    



  def print_matrix(self, matrix, out_file="output.txt"):
    with open(out_file, "w") as file:
      aux = f"\nLa matriz de {len(matrix)} X {len(matrix[0])}\n"
      aux += f"El rango de los valores es {self.lower} - {self.upper}\n"
      print(aux, file=file)
      print(aux)
      if len(matrix) == 0:
        return
      for row in matrix:
        for element in row:
          if element == None:
            print(f"{'-':<6}", end=" ", file=file)
            print(f"{'-':<6}", end=" ")
          else:
            print(f"{element:<6.2f}", end=" ", file=file)
            print(f"{element:<6.2f}", end=" ")  
        print()
        print("", file=file)



  def mean_rows(self, matrix, user, intersecting_columns):
    if len(intersecting_columns) != 0:
      sum = 0
      for i in range(len(matrix[0])):
        if i in intersecting_columns:
          sum += matrix[user][i]
      return sum / len(intersecting_columns)
    return 0



  def intersection_qualified_items(self, u, v):
    intersection_items = []
    row1 = self.matrix[u]
    row2 = self.matrix[v]
    # buscamos los indices de los elementos no nulos
    return [ x for x in range(len(row1)) if self.matrix[u][x] is not None and self.matrix[v][x] is not None]



  def get_neighbors(self, num_neighbor, similarity):
    # Ordena el diccionario por los valores de forma descendente
    ordered_similarity = sorted(similarity, key=lambda x: similarity[x], reverse=True)
    neighbors = dict()
    if num_neighbor == 0:
      return neighbors
    for x in ordered_similarity:
      if self.matrix[x[1]][self.coordinate_prediction[1]] != None:
        neighbors[x] = similarity[x]
        num_neighbor -= 1
      if num_neighbor <= 0:
        break
    return neighbors
  
  
  
  def calculate_priority(self, row):
    return sum(1 for elemento in row if elemento is None)



  def calculate_prediction_queue(self):
    # Crear una lista de tuplas donde el primer elemento es la prioridad y el segundo es la fila
    priority_rows = [(self.calculate_priority(row), index) for index, row in enumerate(self.matrix)]
    # Convertir la lista en una cola de prioridad (heap)
    indices_none = []
    for row in sorted(priority_rows, key=lambda x: x[0]):
      indices_none += [(row[1],indice) for indice, valor in enumerate(self.matrix[row[1]]) if valor is None]
    self.prediction_queue = indices_none
    
    
    
  def normalize(self, matrix):
    result = []
    for row_aux in matrix:
      row = []
      for i in range(len(row_aux)):
        if row_aux[i] != None:
          row.append((row_aux[i] - self.lower) / (self.upper - self.lower))
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
          row.append((row_aux[i] * (self.upper - self.lower)) + self.lower)
        else:
          row.append(None)
      result.append(row)
    return result